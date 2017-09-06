from client import *

token = "52da5ca5454bf583fc7a8d565b3bc311"
name = "sample"
seeds = "http://twitter.com"
api = "analyze"
sample = DiffbotCrawl(token, name, seeds=seeds, api=api)
sample.status()
max = 100
upp = "diffbot"
sample.update(maxToCrawl=max, urlProcessPatter=upp)
sample.download()