from characterai import aiocai, sendCode, authUser
import asyncio

async def main():
    email = input('YOUR EMAIL: ')

    code = sendCode(email)

    print("copy the link as address and paste it here")
    link = input('Link IN MAIL: ')
    token = authUser(link, email)

    print(f'YOUR TOKEN: {token}')
    print("Please save this token for future use")

asyncio.run(main())