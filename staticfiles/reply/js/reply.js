const writeButton = document.getElementById("reply-write");

writeButton.addEventListener("click", async (e) => {
    const replyContent = document.getElementById("reply-content");
    await replyService.write(postId, replyContent.value);
})