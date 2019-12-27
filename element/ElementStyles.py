
from pathlib import Path
styles = {}
element_path = Path(__file__).absolute().parent
styles['MainStyle'] = open(element_path.joinpath('style/MainStyle.qss'), encoding='utf-8').read()
styles['DefaultPushButton'] = open(element_path.joinpath('style/DefaultPushButton.qss'), encoding='utf-8').read()
styles['PrimaryPushButton'] = open(element_path.joinpath('style/PrimaryPushButton.qss'), encoding='utf-8').read()
styles['InfoPushButton'] = open(element_path.joinpath('style/InfoPushButton.qss'), encoding='utf-8').read()
styles['LineEdit'] = open(element_path.joinpath('style/LineEdit.qss'), encoding='utf-8').read()
styles['Label'] = open(element_path.joinpath('style/Label.qss'), encoding='utf-8').read()