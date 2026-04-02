import json
from pathlib import Path
from step_2_1 import OUT_DIR # ㅇㅣ전에 작성한 모듈을 불러옵니다.

OUT_2_3 = OUT_DIR / f'{Path(__file__).stem}.json' #현재 파일명으로 .json 파일 생성

def dump_dirnames(base_dir:Path) -> None:   # 폴더 목록 저장 함수
    dirs=[] #리스트 초기화
    for path in base_dir.iterdir(): 
        if path.is_dir():
            dirs.append(path.as_posix())
    dirs_sorted=sorted(dirs)
    with open(OUT_2_3,'w',encoding='utf-8') as fp:
        json.dump(dirs_sorted,fp,ensure_ascii=False, indent=2)

def load_dirnames() -> list[str]:  # 폴더명 불러오는 함수
    if OUT_2_3.is_file():
        with open(OUT_2_3,encoding='utf-8') as fp:
            return json.load(fp)
    return []

if __name__=='__main__':
    dump_dirnames(Path.home())
