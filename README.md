# uga

---

## 요청사항

### 프린트
- 텍스트를 입력 받아 전표 모양으로 프린트 출력하는 기능

### mysql 입력
- USB 를 체결하면 저장된 파일의 텍스트 수치를 읽어들여 로컬호스트의 mysql 에 insert하는 기능

### PACP (?)

### DCM

cd dcm

```console
pip install -r requirements.txt

# 두번째 인자는 디렉토리
python ./dcm.py tests/1148_DX_1.dcm ./
```