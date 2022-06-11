# 좋은 코드의 일반적인 특징

[![Build Status](https://travis-ci.org/Rainist/python.svg?branch=master)](https://travis-ci.org/Rainist/python)

## 계약에 의한 디자인

```bash
1. 사전조건 - 코드가 실행되기 전 체크, 
  함수가 진행되기 전에 처리 되어야하는 모든 조건을 체크(호출자에게 부과되는 임무)
  
2. 사후조건 - 함수의 반환값이 올바른지 유효성 검사
3. 불변식 - 함수가 실행되는 조건이 일정되게 유지되는지 docstring으로 남겨주는것이 좋다
4. 부작용 - 에러가 발생할 수 있는 사항을 docstring으로 남겨주는것이 좋다
```

### 계약에 의한 디자인(DbC)

```
디자인 원칙이 주된 가치는 문제가 있는 부분을 효과적으로 식별하는데 있다. 
계약을 정의함으로써 런타임 시 오류가 발생했을 때 코드의 어떤 부분이 손상 되었는지
계약이 파손 되었는지가 명확해진다. 
```

프로젝트 이름을 설정할 수 있습니다. 보통의 이름을 적듯 `-` 와 `_` 없이 설정합니다.

```
project_slug [my-python-project]: sample-python
```

프로젝트 폴더 이름을 설정할 수 있습니다. 보통 GitHub Repository로 쓰이는 이름과 같게 설정합니다.

```
package_name [samplepython]: app
```

프로젝트 폴더 안에 파이썬 코드가 담길 패키지 폴더 이름을 설정할 수 있습니다. 이 패키지 이름을 기반으로 `pylint`, 커버리지 측정, `Dockerfile` 설정이 이루어집니다.

```
Select python_version:
1 - 3.7
2 - 3.6
Choose from 1, 2 [1]:
```

사용할 파이썬 런타임 버전을 설정할 수 있습니다. `Dockerfile`, `mypy` 등의 파이썬 버전을 설정하는 데 사용됩니다.

```
use_travis [y]:
```

[`Travis-CI`](https://travis-ci.org) 사용 여부를 설정할 수 있습니다.

* 설정 시 [`codecov`](https://codecov.io)를 사용한 커버리지 측정 관련 내용도 자동으로 추가 된 상태입니다. 커버리지 측정을 원하지 않는다면 `.travis.yml`과 `README.md`에서 관련 내용을 삭제해야합니다.
* `README.md`에 포함된 travis, codecov 뱃지의 URL을 적절하게 수정해야합니다.
* Private project를 생성한다면 `README.md`의 travis, codecov 뱃지, `.travis.yml`의 codecov 부분에 토큰을 추가해야합니다.

```
use_docker [y]:
```

Dockerfile 사용 여부를 설정할 수 있습니다.
- 설정시 `Dockerfile`이 생성됩니다.

```
Select use_mypy:
1 - do not use
2 - beginner
3 - expert
Choose from 1, 2, 3 [1]: 3
```

[`mypy`](https://github.com/python/mypy) 사용 여부를 설정할 수 있습니다. 설정 시 `pre-push` hook과 `make check` 과정에 `mypy` 가 추가됩니다.

* `beginner`: 타입 힌팅이 있는 함수들만 가지고 타입 검사를 수행합니다.
* `expert`: 타입 힌팅이 없는 함수까지 경고를 발생시킵니다.

```
use_black [n]: y
```

[`black`](https://github.com/ambv/black) 사용 여부를 설정할 수 있습니다. 설정 시 `pre-push` hook과 `make check`, `make format` 과정에 `black` 이 추가됩니다.

```
use_pipenv [n]: y
```

[`pipenv`](https://github.com/pypa/pipenv) 사용 여부를 설정할 수 있습니다.

* `black`과 `pipenv`를 같이 사용할 경우, `black`이 현재 프리릴리즈 상태이므로 `pipenv lock --pre` 명령어로 `Pipfile.lock` 파일을 생성해야합니다.
