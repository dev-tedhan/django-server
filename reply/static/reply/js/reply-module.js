const replyService = (() => {
    const write = async (postId, replyContent) => {
        await fetch(`/reply/write/${postId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({ replyContent: replyContent })
        });
    }

    const getList = async (postId, page=1, callback) => {
        const response = await fetch(`/reply/list/${postId}/${page}`);
        const replies = await response.json();
        if(callback){
            return callback(replies);
        }
        return replies;
    }

    return {write: write, getList: getList};
})();