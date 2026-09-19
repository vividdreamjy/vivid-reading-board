body = open('app-body.html', encoding='utf-8').read()
head = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="독서 인증 사진을 날짜별로 모아 누가 인증했고 누가 빠졌는지, 개인별로 얼마나 쌓았는지 한눈에 보여주는 30일 챌린지 보드.">
<meta name="theme-color" content="#FAF7F7">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23C9304B'/%3E%3Cpath d='M9 8h9a5 5 0 0 1 5 5v11H14a5 5 0 0 0-5 5z' fill='none' stroke='white' stroke-width='2.2' stroke-linejoin='round'/%3E%3C/svg%3E">
<style>
:root{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font-size:14px}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
"""
tail = "\n</body>\n</html>\n"
open('index.html','w',encoding='utf-8').write(head + body + tail)
print('ok', len(head+body+tail))
