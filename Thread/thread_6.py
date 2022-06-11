import concurrent.futures
import logging
import threading
import random
import queue
from concurrent.futures import ThreadPoolExecutor
import time

"""
* Parallellism with MultiProcessing
- Parallellism(멀티 코어 = 병렬코어) : 각자가 할 일을 한다. 그래서 각각이 먼저 끝나는 늦게 끝나든 상관없이 돌게된다.

1. Parallellism 
- 완전히 동일한 타이밍(시점)에 태스크 실행
- 다양한 파트(부분)으로 나눠서 실행(합 나눠서 구하고 취합)
- 멀티프로세싱 CPU가 1 core인 경우 만족하지 않음.
- 예시 - 딥러닝, 비트코인 채굴등 사용

2. Process vs Thread 차이 비교 중요함!!
- 독립된 메모리(프로세스), 공유 메모리(스레드)
- 많은 메모리 필요(프로세스), 적은 메모리(스레드)
- 데드 프로세스 생성 가능성 있음, 데드 스레드 생성 쉽지 않음
- 오버 헤드 큼(프로세스), 오버 작음(스레드)
- 생성/소멸 다소 느림(프로세스), 생성 소명 빠름(스레드)
- 코드 작성 쉬움 디버깅 어려움(프로세스), 코드작성 어려움 디버깅 쉬움(스레드)
- 

"""

