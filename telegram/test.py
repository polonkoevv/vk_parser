import vparser
import config
import asyncio
import json

api = vparser.Parser(config.TOKEN)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    global parser
    parser = vparser.Parser(config.TOKEN)
    # And the run events dispatching
    # load_dotenv()
    # token = os.getenv("TOKEN")
    
    # global api
    # api = Api(token=token)
    res = await parser.wallGet("346598810")
    res = await parser.userGet("696996494")
    
    # print(json.dumps(res, indent=4))
    # print(res)
    
    wall = await parser.wallGet('696996494')
    # print(json.dumps(wall, indent=4))
    # print(wall)
    
    photos = await parser.photosGet("696996494")
    print(photos)


if __name__ == "__main__":
    asyncio.run(main())


# activities,about,blacklisted,blacklisted_by_me,books,bdate,can_be_invited_group,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,can_write_private_message,career,common_count,connections,contacts,city,country,crop_photo,domain,education,exports,followers_count,friend_status,has_photo,has_mobile,home_town,photo_100,photo_200,photo_200_orig,photo_400_orig,photo_50,sex,site,schools,screen_name,status,verified,games,interests,is_favorite,is_friend,is_hidden_from_feed,last_seen,maiden_name,military,movies,music,nickname,occupation,online,personal,photo_id,photo_max,photo_max_orig,quotes,relation,relatives,timezone,tv,universities,is_verified