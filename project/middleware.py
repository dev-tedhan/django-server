from django.http import HttpResponseRedirect

from member.models import MemberFile, Member


def pre_handle_request(get_response):
    def middleware(request):
        # cors 해제
        setattr(request, '_dont_enforce_csrf_checks', True)
        # 요청 전처리
        uri = request.get_full_path()
        if request.user_agent.is_mobile:
            print("MOBILE")
            uri = f'/mobile{uri}'
            # 변경된 경로로 요청
            request.path_info = uri
        elif 'admin' not in uri:
            print("PC")
            if "accounts" not in uri:
                uri = uri.replace('/mobile', '')
                # 변경된 경로로 요청
                request.path_info = uri

        # 프로필 경로 세션에 저장
        try:
            member_file = Member.objects.get(id=request.session['id']).memberfile_set.first()
            if member_file is not None:
                request.session['profile'] = str(member_file.image)
        except KeyError:
            pass
        response = get_response(request)
        # 응답 후처리

        return response
    return middleware
