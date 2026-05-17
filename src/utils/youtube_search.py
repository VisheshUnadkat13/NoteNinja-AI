from youtubesearchpython import VideosSearch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_youtube_videos(query, limit=5):
    """
    Searches for YouTube videos based on a query and returns a list of video details.
    
    Args:
        query (str): The search term.
        limit (int): Number of results to return.
        
    Returns:
        list: A list of dictionaries containing video title, link, thumbnail, duration, and views.
    """
    try:
        logger.info(f"Searching YouTube for: {query}")
        videos_search = VideosSearch(query, limit=limit)
        results = videos_search.result()
        
        video_list = []
        if results and 'result' in results:
            for video in results['result']:
                video_data = {
                    'title': video.get('title'),
                    'link': video.get('link'),
                    'thumbnail': video.get('thumbnails', [{}])[0].get('url'),
                    'duration': video.get('duration'),
                    'views': video.get('viewCount', {}).get('short'),
                    'channel': video.get('channel', {}).get('name')
                }
                video_list.append(video_data)
        
        return video_list
    except Exception as e:
        logger.error(f"Error searching YouTube: {str(e)}")
        return []

if __name__ == "__main__":
    # Test the function
    test_query = "oops concept in java"
    videos = search_youtube_videos(test_query)
    for v in videos:
        print(f"Title: {v['title']}\nLink: {v['link']}\n")
