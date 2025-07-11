from enum import Enum


class SupportedMetricNames(Enum):
    TTFT = "ttft"
    TPOT = "tpot"
    E2E = "e2e"
    REQUEST_QUEUE_TIME = "request_queue_time"


class RequestEventTiming(Enum):
    ARRIVAL_TIME = "arrival_time"
    FIRST_TOKEN_TIME = "first_token_time"
    FIRST_SCHEDULED_TIME = "first_scheduled_time"
    LAST_TOKEN_TIME = "last_token_time"
