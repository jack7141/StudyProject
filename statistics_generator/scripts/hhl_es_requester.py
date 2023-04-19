import requests


class HhlESRequester(object):
    fep_url_map = [
        { "endpoint": "fep.customer.contract.list", "name": "보유계약 목록 조회" },
        { "endpoint": "fep.customer.contract.detail", "name": "보유계약 상세 조회" },
        { "endpoint": "fep.contract.fund.list", "name": "계약별 펀드정보 조회" },
        { "endpoint": "fep.contract.fund.yield", "name": "계약별 펀드 수익률 조회" },
        { "endpoint": "fep.contract.yield", "name": "계약별 수익률 리스트 조회" },
        { "endpoint": "fep.auth.kakaopay.init",  "name": "최초인증 요청" },
        { "endpoint": "fep.auth.kakaopay.checkin", "name": "재인증 요청" },
        { "endpoint": "fep.auth.kakaopay.status.check",  "name": "인증상태 조회" },
        { "endpoint": "fep.auth.kakaopay.status.verify",  "name": "인증결과 확인" },
        { "endpoint": "fep.auth.fount.register",  "name": "고객등록 요청" },
        { "endpoint": "fep.auth.fount.delete",  "name": "고객 ID 삭제 요청" },
        { "endpoint": "fep.customer.setting",  "name": "고객 및 계약 각종 설정" } 
    ]
        
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token
        self.endpoints = [entry['endpoint'] for entry in self.fep_url_map]
        
    def _get_es_search_query(self, endpoint):
        return {
            "_source": ["timestamp", "from"],
            "size": 20,
            "query": {
                "bool": {
                    "must": [
                        { 
                            "match": {
                                "from": endpoint
                            }
                        },
                        {
                            "range": {
                                "timestamp": {                
                                    "gte": "now-1w/w",
                                    "lte": "now/d"
                                }
                            }
                        }
                    ]
                }
            }
        }
        
    def _get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.token}",
        }
    
    def _request(self, query_body):
        response = requests.get(
            url=self.api_url, 
            json=query_body, 
            headers=self._get_headers()
        )
        if not response.ok:
            raise ValueError(f'FAILED GET DATA, QUERY_BODY : {query_body}')
        
        return response.json()
    
    def get_hits(self, query_body):
        response = self._request(query_body=query_body)
        return response['hits']['total']['value']
    
    def get_hits_all_api(self):
        ret = []
        for endpoint in self.endpoints:        
            query_body = self._get_es_search_query(endpoint)
            hits = self.get_hits(query_body)
                    
            name = [entry['name'] for entry in self.fep_url_map if entry['endpoint'] == endpoint][0]
            ret.append({'NAME': name, 'COUNT': hits})
        
        return ret