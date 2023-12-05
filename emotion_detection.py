import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

def emotion_from_string(input_str):
    res = None
    samples = [
        input_str,
        input_str
    ]

    async def main():
        try:
            client = HumeStreamClient("ENTER KEY HERE")
            config = LanguageConfig()
            async with client.connect([config]) as socket:
                for i in range(1):
                    result = await socket.send_text(samples[i])
                    emotions = result["language"]["predictions"][0]["emotions"]
                    max_em = max(emotions, key=lambda x: x['score'])
                    res = list(max_em.values())[0]
                    print(list(max_em.values())[0])
            return res
        except websockets.ConnectionClosed:
            print("Connection closed")
            main()
        except asyncio.TimeoutError:
            print("Timeout occurred")
            return "Entrancement"

    return asyncio.run(main())

    
    

#emotion_from_string("Hello, how are you?")
