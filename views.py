from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_protect

def chat_page(request):
    try:
        descope_client = DescopeClient(project_id='P2U3izm3RD0Rx2NYuRlGzIeJFCyg')
        session_token = request.GET.get('sessionToken')
        print(session_token)
        try:
            jwt_response = descope_client.validate_session(session_token=session_token)
            print("Successfully validated user session:")
            print(jwt_response)
            return render(request, 'chat.html')
        except Exception as error:
            print("Could not validate user session. Error:")
            print(error)
            
    except Exception as error:
        print("failed to initialize. Error:")
        print(error)

    return render(request, 'login.html')

def login_page(request):
    return render(request, 'login.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient
)
from .models import QABotCache

# @csrf_exempt
# def process_question(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         question = data.get('question', '')

#         # Get the answer from the QABotCache
#         answer = QABotCache.get_answer(question)

#         # Construct and return a JSON response
#         response_data = {'answer': answer}
#         return JsonResponse(response_data)

from django.http import JsonResponse

# @csrf_exempt
# def process_question(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         question = data.get('question', '')

#         # Get the answer from the QABotCache
#         answer = QABotCache.get_answer(question)

#         # Construct and return a JSON response
#         response_data = {'answer': answer}
#         return JsonResponse(response_data)
#     else:
#         # Handle the case when the request method is not 'POST'
#         response_data = {'error': 'Invalid request method'}
#         return JsonResponse(response_data, status=405)  # 405 Method Not Allowed

@csrf_exempt
def process_question(request):
    print(request)
    print("r",request.body)

    if request.method == 'POST' :
        data = json.loads(request.body.decode('utf-8'))
        question = data.get('question', '')

        # Get the answer from the QABotCache
        answer = QABotCache.get_answer(question)

        # Return the answer using the template
        response_data = {'answer': answer}
        return JsonResponse(response_data)
    else:
        # Handle the case when the request method is not 'POST'
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=405)  # 405 Method Not Allowed


def validate_session(request, descope_client):
    # Fetch session token from HTTP Authorization Header
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        session_token = auth_header.split(' ')[1]
        try:
            jwt_response = descope_client.validate_session(session_token=session_token)
            print("Successfully validated user session:")
            print(jwt_response)
            return True
        except Exception as error:
            print("Could not validate user session. Error:")
            print(error)
            return False