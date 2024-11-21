import json
import pandas as pd
import re
import copy
from collections import Counter

import boto3
from typing import List
from langchain.llms.bedrock import Bedrock
from botocore.config import Config
import time
import os


def invoke_claude_base(client, 
                       messages = [{"role": "user", "content": [{"type": "text", "text": "Hello!"}]}],
                       system = "You are an assistant.",
                       model_id="anthropic.claude-3-sonnet-20240229-v1:0", 
                       max_tokens=1024, 
                       temperature = 1.0, 
                       top_k = None, 
                       top_p = None,
                       stop_sequences=["Human:"],
                       use_streaming = False,
                       anthropic_version = "bedrock-2023-05-31",
                       print_details = True):
    """
    Invokes Anthropic Claude models to run an inference using the input
    provided in the request body.

    :param prompt: The prompt that you want Claude LLM to complete.
    :return: Inference response from the model.
    """

    # Invoke Claude models with the text prompt
    
    body = {
        "anthropic_version": anthropic_version,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages,
    }
    
    if system is not None: 
        body["system"]= system
    if top_k is not None: 
        body["top_k"]= top_k
    if top_p is not None: 
        body["top_p"]= top_p
    if stop_sequences is not None:    
        body["stop_sequences"] = stop_sequences
    
    time0 = time.time()
    if use_streaming:
        response = client.invoke_model_with_response_stream(
            modelId=model_id,
            body=json.dumps(body),
        )
        stream = response.get("body")
        output_text = ""
        la = True
        if stream:
            for event in stream:
                chunk = event.get("chunk")
                if chunk:
                    if la:
                        start_time = time.time() - time0
                        print(f"Response(s):")
                        #print(f"\n**** Stream Start {start_time} ****\n")
                        la = False
                    chunk_obj = json.loads(chunk.get("bytes").decode())
                    #print(chunk_obj)
                    if chunk_obj["type"]=="content_block_delta":
                        text = chunk_obj["delta"]["text"]
                        print(text, end="")
                        output_text = output_text + text
                    if chunk_obj["type"]=="message_stop":
                        input_tokens = chunk_obj["amazon-bedrock-invocationMetrics"]["inputTokenCount"]
                        output_tokens = chunk_obj["amazon-bedrock-invocationMetrics"]["outputTokenCount"]
                        latency_start = chunk_obj["amazon-bedrock-invocationMetrics"]["firstByteLatency"]/1000
                        latency_end = chunk_obj["amazon-bedrock-invocationMetrics"]["invocationLatency"]/1000
        end_time = time.time() - time0
        output_list = [output_text]
        #print(f"\n**** Stream End {end_time} ****\n")
        print("\n")
    else:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(body),
        )
        end_time = time.time() - time0
        latency_start = end_time
        latency_end = end_time

        # Process and print the response
        result = json.loads(response.get("body").read())
        input_tokens = result["usage"]["input_tokens"]
        output_tokens = result["usage"]["output_tokens"]
        output_list = result.get("content", [])
        output_text = "\n".join([x["text"] for x in output_list])
        print(f"Response(s):")
        print(output_text)

    if print_details:
        print("Latency details:")
        print(f"- The streaming start latency is {latency_start} seconds.")
        print(f"- The full invocation latency is {latency_end} seconds.")

        print("Invocation details:")
        print(f"- The input length is {input_tokens} tokens.")
        print(f"- The output length is {output_tokens} tokens.")
    
    output_obj = {
        "response_text": output_text,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "latency_start": latency_start,
        "latency_end": latency_end,
    }

    return output_obj