from drf_yasg import openapi


# 스웨거에서 query 파라미터를 입력받을 수 있기 위해 추가함. 없애도 됨
param_hashtags = openapi.Parameter(
    'hashtags',
    openapi.IN_QUERY,
    description='filter',
    type=openapi.TYPE_STRING
)

# 스웨거에서 query 파라미터를 입력받을 수 있기 위해 추가함. 없애도 됨
param_search = openapi.Parameter(
    'search',
    openapi.IN_QUERY,
    description='filter',
    type=openapi.TYPE_STRING
)

# 스웨거에서 query 파라미터를 입력받을 수 있기 위해 추가함. 없애도 됨
param_orderby = openapi.Parameter(
    'orderby',
    openapi.IN_QUERY,
    description='filter',
    type=openapi.TYPE_STRING
)