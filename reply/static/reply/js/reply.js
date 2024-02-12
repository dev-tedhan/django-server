let page = 1

const moreButton = document.getElementById("more-replies");

// 더보기 버튼 보이기
// replyService.getList(postId, page + 1).then((replies) => {
//     console.log(replies)
//     if(replies.length !== 0){
//         moreButton.style.display = "flex";
//     }
// });

const showList = (replies) => {
    let text = ``;
    replies.forEach((reply) => {
        text += `
            <li>
                <div>
                    <section class="content-container">
                        <div class="profile">
                            <div><img src="/upload/${reply.image}" width="15px"></div>
                            <h6 class="writer">${reply.member_name}</h6>
                        </div>
                        <h4 class="title">${reply.reply_content}</h4>
                        <section class="reply-update-wrap">
                            <textarea id="" cols="30" rows="1" placeholder="내 댓글">${reply.reply_content}</textarea>
                            <div class="button-wrap">
                                <button class="update-done">작성완료</button>
                                <button class="calcel">취소</button>
                            </div>
                        </section>
                        <h6 clss="post-info">
                            <span class="date">${timeForToday(reply.created_date)}</span>
        `;
        if(reply.member__id == memberId) {
            text += `
                            <span class="date">·</span>
                            <span class="update">수정</span>
                            <span class="date">·</span>
                            <span class="delete">삭제</span>
            `
        }
        text += `
                        </h6>
                    </section>
                </div>
            </li>
        `;
    });
    return text;
}
// 최초 1페이지 목록 불러오기
replyService.getList(postId, page, showList).then((text) => {
    const repliesLayout = document.querySelector("#replies-wrap ul");
    repliesLayout.innerHTML = text;
});

// 무한 스크롤
window.addEventListener('scroll', async (e) => {
    // innerHeight: 창 틀을 뺀 내용부분의 높이(고정값)
    // scrollY: 이동한 높이
    // offsetHeight: 전체 높이(고정값)
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        const replies = await replyService.getList(postId, page);
        if(replies.length === 0){
            return;
        }
        const repliesLayout = document.querySelector("#replies-wrap ul");
        page++;
        const text = await replyService.getList(postId, page, showList);
        repliesLayout.innerHTML += text;
    }
})

// 더보기 버튼
// moreButton.addEventListener("click", async (e) => {
//     const repliesLayout = document.querySelector("#replies-wrap ul");
//     page++;
//     const text = await replyService.getList(postId, page, showList);
//     // 더보기 클릭 시, 기존 내용 밑에 다음 페이지 내용 추가
//     repliesLayout.innerHTML += text;
//     const replies = await replyService.getList(postId, page + 1);
//     if(replies.length === 0){
//         moreButton.style.display = "none";
//     }
// });


const writeButton = document.getElementById("reply-write");

writeButton.addEventListener("click", async (e) => {
    const repliesLayout = document.querySelector("#replies-wrap ul");
    const replyContent = document.getElementById("reply-content");
    await replyService.write(postId, replyContent.value);
    replyContent.value = "";
    page = 1;
    const text = await replyService.getList(postId, page, showList);
    // 작성 완료 후 1페이지 내용 재조회
    repliesLayout.innerHTML = text;
    const replies = await replyService.getList(postId, page + 1);
    if(replies.length !== 0){
        moreButton.style.display = "block";
    }
});

function timeForToday(datetime) {
    const today = new Date();
    const date = new Date(datetime);

    let gap = Math.floor((today.getTime() - date.getTime()) / 1000 / 60);

    if (gap < 1) {
        return "방금 전";
    }

    if (gap < 60) {
        return `${gap}분 전`;
    }

    gap = Math.floor(gap / 60);

    if (gap < 24) {
        return `${gap}시간 전`;
    }

    gap = Math.floor(gap / 24);

    if (gap < 31) {
        return `${gap}일 전`;
    }

    gap = Math.floor(gap / 31);

    if (gap < 12) {
        return `${gap}개월 전`;
    }

    gap = Math.floor(gap / 12);

    return `${gap}년 전`;
}

