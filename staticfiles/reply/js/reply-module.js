const replyService = (() => {
    const write = async (postId, replyContent) => {
        await fetch(`/reply/write/${postId}`, {
            method: "POST",
            body: {replyContent: replyContent}
        })
    }

    return {write: write};
})();