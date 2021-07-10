# 실행환경
python 3.7 / tenserflow = 1.15

현재 코드는 tenserflow 1 버전에서 동작하는 코드입니다.  
python 3.8 이상에서는 tenserflow 1.버전이 pip으로 다운이 안되므로  
python 3.8 미만의 버전에서 사용해야 합니다.

## 1. 가상환경 셋팅
1. python -m venv venv      (가상환경 생성 // manage.py가 있는 곳에서 실행)  
2. os에 맞는 가상환경 실행  
2-1. source venv/bin/activate (mac에서 가상환경 실행)  
2-2. source venv/Scripts/activate (window에서 가상환경 실행)

## 2. 라이브러리 설치
1. pip install -r requirements.txt (코드실행에 필요한 라이브러리 다운)

## 3. 서버 실행
1. python manage.py migrate (최초 1번)
2. python manage.py runserver (로컬에서 서버 실행)

<br>  


### synthesizer.py 실행
tocotron/app/tacotron2 경로에서 <b>python synthesizer.py</b> 실행  


 
 