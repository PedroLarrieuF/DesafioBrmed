from django.shortcuts import render
from datetime import date,datetime
from django.contrib import messages
from .models import Base_rates
import requests
import json
import urllib.parse



class Utils():

    today = (date.today())
    url = 'https://api.vatcomply.com/rates?'
    base = 'USD'

def latest_5_days(request):
    
    if request.method == 'GET':
        day_strip = datetime.strptime(str(Utils.today),'%Y-%m-%d').day
        month_strp = datetime.strptime(str(Utils.today),'%Y-%m-%d').month
        year_strp = datetime.strptime(str(Utils.today),'%Y-%m-%d').year
        return render(request, 'homepage.html', {'today': Utils.today, 'day':day_strip, 'month': month_strp})


    if request.method == 'POST':
        url_api = Utils.url + urllib.parse.urlencode({'date': Utils.today , 'base': Utils.base})
        api_response = requests.get(url_api)
        api_response_content = json.loads(api_response.content)
        base_rates = api_response_content['rates']
        day_strip = datetime.strptime(str(Utils.today),'%Y-%m-%d').day
        month_strp = datetime.strptime(str(Utils.today),'%Y-%m-%d').month
        year_strp = datetime.strptime(str(Utils.today),'%Y-%m-%d').year
        jpy_list = []
        eur_list = []
        usd_list = []
     
        for countrys in base_rates:
            if countrys == 'USD':   
                value_usd = api_response_content['rates']['USD']
                values_format_usd = "{:.2f}".format(value_usd)
                         
            if countrys == 'EUR':
                value_eur = api_response_content['rates']['EUR']
                values_format_eur = "{:.2f}".format(value_eur)

            if countrys == 'JPY':
                values_jpy = api_response_content['rates']['JPY']   
                values_format_jpy = "{:.2f}".format(values_jpy)
            

        custom_data_response = request.POST.get('days')
        custom_data_response_strp = datetime.strptime(str(custom_data_response), '%Y-%m-%d').day
        custom_data_response_strp_year = datetime.strptime(str(custom_data_response), '%Y-%m-%d').year
        custom_data_response_strp_month = datetime.strptime(str(custom_data_response), '%Y-%m-%d').month

        week_day = day_strip - custom_data_response_strp

        if custom_data_response_strp_year == year_strp and custom_data_response_strp_month == month_strp and week_day < 5:
                url_api = Utils.url + urllib.parse.urlencode({'date': custom_data_response, 'base': Utils.base})
                api_response = requests.get(url_api)
                api_response_content = json.loads(api_response.content)
                base_rates = api_response_content['rates']

                for countrys in base_rates:
                    if countrys == 'USD':   
                        value_usd = api_response_content['rates']['USD']
                        values_format_usd = "{:.2f}".format(value_usd)
                                
                    if countrys == 'EUR':
                        value_eur = api_response_content['rates']['EUR']
                        values_format_eur = "{:.2f}".format(value_eur)

                    if countrys == 'JPY':
                        values_jpy = api_response_content['rates']['JPY']   
                        values_format_jpy = "{:.2f}".format(values_jpy)

                if not(Base_rates.objects.filter(date = custom_data_response)):
                    Base_rates.objects.create(
                        date = str(custom_data_response),
                        usd_value = str(values_format_usd),
                        jpy_value = str(values_format_eur),
                        eur_value = str(values_format_jpy)
                    )
                
                jpy_value_list_get = Base_rates.objects.all().values_list('jpy_value',flat=True)
                usd_value_list_get = Base_rates.objects.all().values_list('usd_value', flat = True)
                eur_value_list_get = Base_rates.objects.all().values_list('eur_value', flat = True)
                
            
                for x in jpy_value_list_get:
                 jpy_float_list = float(x)
                 jpy_list.append(jpy_float_list)

                for x in usd_value_list_get:
                 usd_float_list = float(x)
                 usd_list.append(usd_float_list)

                for x in eur_value_list_get:
                 eur_value_list = float(x)
                 eur_list.append(eur_value_list) 
            
       

                print('foram criados: ', Base_rates.objects.count())
            

        return render(request, 'homepage.html', {'custom_data_response':custom_data_response,'today': Utils.today,'day':day_strip, 'month': month_strp, 'jpy': jpy_list, 'eur': eur_list, 'usd': usd_list, 'eur': eur_list})