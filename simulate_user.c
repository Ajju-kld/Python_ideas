#include <stdio.h>
#include <windows.h>
#include <wininet.h>
#include <process.h>

#define API_ENDPOINT L"https://api.140.ieeer10.org/api"
#define NUM_USERS 1000000

DWORD WINAPI send_request(LPVOID url)
{
    HINTERNET hInternet, hConnect;
    DWORD dwSize = sizeof(DWORD);
    DWORD dwStatusCode = 0;

    // Initialize WinINet
    hInternet = InternetOpenW(L"User-Agent", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    if (hInternet == NULL)
    {
        printf("InternetOpen failed: %lu\n", GetLastError());
        return 1;
    }

    // Connect to the API endpoint
    hConnect = InternetOpenUrlW(hInternet, (LPCWSTR)url, NULL, 0, INTERNET_FLAG_RELOAD, 0);
    if (hConnect == NULL)
    {
        printf("InternetOpenUrl failed: %lu\n", GetLastError());
        InternetCloseHandle(hInternet);
        return 1;
    }

    // Get the HTTP response status code
    if (!HttpQueryInfo(hConnect, HTTP_QUERY_STATUS_CODE | HTTP_QUERY_FLAG_NUMBER, &dwStatusCode, &dwSize, NULL))
    {
        printf("HttpQueryInfo failed: %lu\n", GetLastError());
    }
    else if (dwStatusCode == 200)
    {
        printf("Request sent and received successfully.\n");
    }

    // Cleanup
    InternetCloseHandle(hConnect);
    InternetCloseHandle(hInternet);

    return 0;
}

int main()
{
    HANDLE threads[NUM_USERS];
    int i;

    // Create threads to send requests
    for (i = 0; i < NUM_USERS; i++)
    {
        threads[i] = CreateThread(NULL, 0, send_request, (LPVOID)API_ENDPOINT, 0, NULL);
        if (threads[i] == NULL)
        {
            printf("Error creating thread\n");
            return 1;
        }
    }

    // Wait for threads to finish
    WaitForMultipleObjects(NUM_USERS, threads, TRUE, INFINITE);

    return 0;
}
