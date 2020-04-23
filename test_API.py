import json
import unittest
from unittest.mock import patch
from APIwrap.API import wrapper


class TestingAPI(unittest.TestCase):

    def test_getByName1(self):

        fake_json = [{'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY', 'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000, 'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8, 'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e', 'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto', 'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'}, 'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'EGY'}]

        obj = wrapper()
        result = obj.getName('Egypt')
        print(result)

        self.assertEqual(result, fake_json)

    def test_name2(self):

        obj = wrapper()
        result = obj.getName('nowhere')

        fake_json={'status': 404, 'message': 'Not Found'}


        print(result)

        self.assertEqual(result, fake_json)


    def test_alpha1(self):
        obj = wrapper()
        result=obj.getalpha('EG')
        print(result)
        fake_json={'alpha2Code':'EGY'}
        self.assertTrue('alpha2Code' in result)
        self.assertEqual(result['alpha2Code'], 'EG')

    def test_alpha2(self):
        obj = wrapper()
        result = obj.getalpha('Moo')
        fake_json = {'status': 404, 'message': 'Not Found'}


        self.assertEqual(result,fake_json)

    def test_currency1(self):
        obj = wrapper()
        result = obj.getcurrency('EGP')
        fake_json = [{'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY', 'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000, 'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8, 'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e', 'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto', 'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'}, 'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'EGY'}]

        self.assertEqual(result,fake_json)

    def test_currency2(self):
        obj = wrapper()
        result=obj.getcurrency('haha')
        fake_json =  {'status': 400, 'message': 'Bad Request'}

        self.assertEqual(fake_json,result)

    def test_currency3(self):
        obj = wrapper()
        result = obj.getcurrency('haha')
        fake_json = {'message': 'Bad Request', 'status': 400}
        self.assertEquals(result,fake_json)


    def test_getSpecific1(self):
        obj = wrapper()
        result=obj.getSpecific('Egypt','alpha2Code')
        expected='alpha2Code= EG'
        self.assertEqual(result,expected)

    def test_getSpecific2(self):
        obj = wrapper()
        result=obj.getSpecific('Egypt','alpha3Code')
        expected='alpha3Code= EGY'
        self.assertEqual(result,expected)

    def test_callingCode1(self):
        obj = wrapper()
        result=obj.getcallingcode('20')
        expected = [{'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY', 'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000, 'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8, 'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e', 'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto', 'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'}, 'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'EGY'}]

        self.assertEqual(result,expected)


    def test_callingCode2(self):
        obj = wrapper()
        result = obj.getcallingcode('804')
        expected = {'status': 404, 'message': 'Not Found'}
        self.assertEqual(result,expected)

    def test_capital(self):
        obj= wrapper()
        result= obj.getcapital('Cairo')
        expected = [{'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY', 'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000, 'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8, 'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e', 'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto', 'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'}, 'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'EGY'}]
        self.assertEqual(result,expected)

    def test_capital2(self):
        obj=wrapper()
        result=obj.getcapital('hahaha')
        expected = {'status': 404, 'message': 'Not Found'}
        self.assertEqual(result,expected)

    def test_region(self):
        obj = wrapper()
        result= obj.getregion('Africa')
        expected = {'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY', 'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'], 'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000, 'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8, 'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e', 'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}], 'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}], 'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto', 'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'}, 'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [{'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [], 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana', 'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [], 'otherNames': ['جامعة الدول العربية', 'Jāmiʻat ad-Duwal al-ʻArabīyah', 'League of Arab States']}], 'cioc': 'EGY'}
        self.assertIn(expected,result)


    def test_region2(self):
        obj = wrapper()
        result=obj.getregion('malala')
        expected = {'status': 404, 'message': 'Not Found'}
        self.assertEqual(result,expected)

    def test_getByNameIntegration(self):
        fake_json = [{'name': 'Egypt', 'topLevelDomain': ['.eg'], 'alpha2Code': 'EG', 'alpha3Code': 'EGY',
                      'callingCodes': ['20'], 'capital': 'Cairo', 'altSpellings': ['EG', 'Arab Republic of Egypt'],
                      'region': 'Africa', 'subregion': 'Northern Africa', 'population': 91290000,
                      'latlng': [27.0, 30.0], 'demonym': 'Egyptian', 'area': 1002450.0, 'gini': 30.8,
                      'timezones': ['UTC+02:00'], 'borders': ['ISR', 'LBY', 'SDN'], 'nativeName': 'مصر\u200e',
                      'numericCode': '818', 'currencies': [{'code': 'EGP', 'name': 'Egyptian pound', 'symbol': '£'}],
                      'languages': [{'iso639_1': 'ar', 'iso639_2': 'ara', 'name': 'Arabic', 'nativeName': 'العربية'}],
                      'translations': {'de': 'Ägypten', 'es': 'Egipto', 'fr': 'Égypte', 'ja': 'エジプト', 'it': 'Egitto',
                                       'br': 'Egito', 'pt': 'Egipto', 'nl': 'Egypte', 'hr': 'Egipat', 'fa': 'مصر'},
                      'flag': 'https://restcountries.eu/data/egy.svg', 'regionalBlocs': [
                {'acronym': 'AU', 'name': 'African Union', 'otherAcronyms': [],
                 'otherNames': ['الاتحاد الأفريقي', 'Union africaine', 'União Africana', 'Unión Africana',
                                'Umoja wa Afrika']}, {'acronym': 'AL', 'name': 'Arab League', 'otherAcronyms': [],
                                                      'otherNames': ['جامعة الدول العربية',
                                                                     'Jāmiʻat ad-Duwal al-ʻArabīyah',
                                                                     'League of Arab States']}], 'cioc': 'EGY'}]

        obj = wrapper()
        result = obj.getName('Egypt')
        print(result)

        self.assertEqual(result, fake_json)

if __name__ == "__main__":
    unittest.main()