import requests

basic = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA1OTM2NDUxLCJpYXQiOjE3MDUzMzY0NTEsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjIyYmVjNTM4LTU5NjAtNGU3OC05MTJhLTljMDY2MGZhYWQxOSIsImVtYWlsIjoibWFzbG92YW9zOTNAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6eyJmdWxsX25hbWUiOiJPbGdhIFYifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJwYXNzd29yZCIsInRpbWVzdGFtcCI6MTcwNTMzNjQ1MX1dLCJzZXNzaW9uX2lkIjoiNzRiN2M5NWItMzFkYS00MzliLTk2NTgtYTQyYWZkYzczY2JlIn0.J2Lnl1qEN4frX95zgDzZHd2y2HmEEJKls7Qq7SWHeSs"
}

response = requests.post(
    url="https://release-gs.qa-playground.com/api/v1/setup",
    headers=basic
)

#
# response = requests.get(
#     url="https://release-gs.qa-playground.com/api/v1/users",
#     headers=basic
# )
# print(response.json())

#
# response = requests.get(
#     url="https://release-gs.qa-playground.com/api/v1/users/db7409f3-be29-47e0-a63f-974f587ba7cb/wishlist",
#     headers=basic
# )
# print(response.json())


#
# response = requests.post(
#     url="https://release-gs.qa-playground.com/api/v1/users/db7409f3-be29-47e0-a63f-974f587ba7cb/wishlist/add",
#     headers=basic,
#     json={
#         "item_uuid": "cb620f56-daa4-43e0-b4a0-e80f8e5be279"
#     }
# )
# print(response.text)
# print(response.status_code)

# response = requests.delete(
#     url="https://release-gs.qa-playground.com/api/v1/users/285c8d21-87cd-44b7-ad09-94cc470a3af7",
#     headers=basic
# )
# # print(response.text)
# print(response.status_code)

#
# response = requests.get(
#     url="https://release-gs.qa-playground.com/api/v1/users",
#     headers=basic
# )
# print(response.json())

# response = requests.get(
#     url="https://release-gs.qa-playground.com/api/v1/games/search",
#     headers=basic,
#     params={
#         "query": "Atomic"
#     }
# )
# print(response.text)
# print(response.status_code)