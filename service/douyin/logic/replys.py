from .common import common_request
def request_replys(video_id: str, comment_id: str, cookie: str, offset: int = 0, limit: int = 20) -> tuple[dict, bool]:
    """
    请求抖音获取评论回复信息
    """
    params = {"cursor": offset, "count": limit, "item_type": 0, "item_id": video_id, "comment_id": comment_id}
    headers = {"cookie": cookie}
    resp, succ = common_request('/aweme/v1/web/comment/list/reply/', params, headers)
    if not succ:
        return resp, succ
    ret = resp.get('comments', {})
    return ret, succ