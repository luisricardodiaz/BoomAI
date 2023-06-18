import asyncio

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

def emotion_from_string(str):
    res = ''
    samples = [
        str,
        str
    ]

    async def main():
        client = HumeStreamClient("j1JhMybzjU9RosGtVyF5qz50pCS5hRSzGZXzGYAFCy7erFrV")
        config = LanguageConfig()
        async with client.connect([config]) as socket:
            for i in range(1):
                result = await socket.send_text(samples[i])
                emotions = (result["language"]["predictions"][0]["emotions"])
                # for x in emotions:
                #     print(x['name'])
                max_em = max(emotions, key=lambda x:x['score'])
                print(list(max_em.values())[0])
            return list(max_em.values())[0]

    return asyncio.run(main())
    
    

#emotion_from_string("Hello, how are you?")