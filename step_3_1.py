import json
from pathlib import Path
from step_2_1 import OUT_DIR # 이전에 작성한 모듈을 불러옴
from step_2_4 import load_filesize_per_dir

OUT_3_1=OUT_DIR / f'{Path(__file__).stem}.json'

def dump_plot_data():  # 데이터 전처리 함수 생성
    size_per_path=load_filesize_per_dir()
    size_per_stem={Path(path).stem:size for path, 
                   size in size_per_path.items() 
                   if size>0}  # 크기가 0보다 큰 폴더만 추출
    plot_data = dict(
        stem=list(size_per_stem.keys()),
        size=list(size_per_stem.values()),
    )
    with open(OUT_3_1,'w',encoding='utf-8') as fp:  #stem, size를 키값으로 하는 딕셔너리 생성
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)

def load_plot_data() -> dict:  #OUT_3_1 경로에 저장된 데이터 불러와서 반환하는 함수 생성 
    if OUT_3_1.is_file():
        with open(OUT_3_1,encoding='utf-8') as fp:
            return json.load(fp)
    return{}

if __name__=='__main__':
    dump_plot_data()
