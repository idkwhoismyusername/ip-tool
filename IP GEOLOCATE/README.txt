Thank you for using my tool!

Setup:

Install Python 3: Make sure you have Python 3 installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Run setup.bat

Get API key: You need to get an API key from RapidAPI to use the IP reputation and geolocation API. Follow these steps to get the API key:

    Go to the following website: https://rapidapi.com/Top-Rated/api/ip-reputation-geoip-and-detect-vpn/pricing

    Make an account for rapidapi.com
    
    Click on the "pricing" tab and select a plan that suits your needs.(Basic one for poor mfs)

    Click on the "subscribe to test" button and create an account if you don't have one already.

    Once you have subscribed to the API, you will get an API key. Copy the API key and save it somewhere safe.

Update the script: Open the script file in a text editor and replace the API key in the headers dictionary with your own API key.

headers = {
    "X-RapidAPI-Key": "your-api-key-here",
    "X-RapidAPI-Host": "ip-reputation-geoip-and-detect-vpn.p.rapidapi.com"
}

Run the script:Run run.bat

    Enter IP addresses: The script will prompt you to enter the IP addresses for which you want to get the information. Enter the IP addresses one by one and press enter after each IP address.

    View results: The script will save the results in a JSON file named "ip.json" and any errors encountered while processing the IP addresses will be saved in a text file named "error.txt" in the same directory. You can view the results and errors by opening these files in a text editor.

That's it! You have successfully set up and used the IP reputation and geolocation tool. If you have any issues or questions, feel free to ask for help.(* always#0001)