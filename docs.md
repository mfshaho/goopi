# Goopi API Documentation

## /gnews Endpoint

This endpoint allows you to retrieve the newest top news related to a specific search term from Google News.

### Request

- **Method:** `GET`
- **URL:** `/gnews`
- **Query Parameters:**
  - `q`: (required) The search term for Google News.

### Example

> **GET** /gnews?q=technology

**Response:**

```json
[
  {
    "title": "السبت المقبل .. البرلمان العراقي يقرر عقد جلسة لانتخاب رئيس جديد",
    "desc": null,
    "date": "12 hours ago",
    "datetime": "2024-05-13T21:38:32.162562",
    "link": "news.google.com/articles/CBMi6AJodHRwczovL3d3dy5wYXJsbWFueS5jb20vTmV3cy81LzU0NzY0OS8lRDglQTclRDklODQlRDglQjMlRDglQTglRDglQUEtJUQ4JUE3JUQ5JTg0JUQ5JTg1JUQ5JTgyJUQ4JUE4JUQ5JTg0LSVEOCVBNyVEOSU4NCVEOCVBOCVEOCVCMSVEOSU4NCVEOSU4NSVEOCVBNyVEOSU4Ni0lRDglQTclRDklODQlRDglQjklRDglQjElRDglQTclRDklODIlRDklOEEtJUQ5JThBJUQ5JTgyJUQ4JUIxJUQ4JUIxLSVEOCVCOSVEOSU4MiVEOCVBRi0lRDglQUMlRDklODQlRDglQjMlRDglQTktJUQ5JTg0JUQ4JUE3JUQ5JTg2JUQ4JUFBJUQ4JUFFJUQ4JUE3JUQ4JUE4LSVEOCVCMSVEOCVBNiVEOSU4QSVEOCVCMy0lRDglQUMlRDglQUYlRDklOEElRDglQUbSAQA?hl=en-US&gl=US&ceid=US%3Aen",
    "img": "news.google.com/api/attachments/CC8iK0NnNDVZMEZoYVMxRWJYSkVZV2x0VFJDdUFSaWlBaWdCTWdZQkpvNkpJZ2s=-w200-h112-p-df",
    "media": "برلمانى",
    "site": null,
    "reporter": null
  }
]
```

---

## /extractor Endpoint

This endpoint extracts data from a given Google News URL.

### Request

- **Method:** `GET`
- **URL:** `/extractor`
- **Query Parameters:**
  - `initial_url`: (required) The URL of the Google News article to extract data from.

### Example

> **GET** /extractor?initial_url=https://news.google.com/articles/article123

**Response:**

```json
{
  "title": "السبت المقبل .. البرلمان العراقي يقرر عقد جلسة لانتخاب رئيس جديد",
  "description": "تأجلت عدة مرات جلسات لاختيار رئيس جديد للبرلمان العراقي منذ نوفمبر الماضي ، عندما قضت المحكمة الاتحادية العليا بإنهاء عضوية رئيس البرلمان محمد الحلبوسي في مجلس النواب في أعقاب شكوى قدمها ضده نائب سابق اتهمه فيها بالتزوير",
  "content": [
    "تأجلت عدة مرات جلسات لاختيار رئيس جديد للبرلمان العراقي منذ نوفمبر الماضي ، عندما قضت المحكمة الاتحادية العليا بإنهاء عضوية رئيس البرلمان محمد الحلبوسي في مجلس النواب في أعقاب شكوى قدمها ضده نائب سابق اتهمه فيها بالتزوير",
    "",
    "وأفادت وكالة الأنباء العراقية، اليوم الاثنين، بأن البرلمان العراقي قرر عقد جلسة لانتخاب رئيس له يوم السبت المقبل.",
    "",
    "وتأجلت عدة مرات جلسات لاختيار رئيس جديد للبرلمان العراقي منذ نوفمبر تشرين الثاني عندما قضت المحكمة الاتحادية العليا بإنهاء عضوية رئيس البرلمان محمد الحلبوسي في مجلس النواب في أعقاب شكوى قدمها ضده نائب سابق اتهمه فيها بالتزوير.",
    "",
    "ويعدّ منصب رئيس البرلمان من حصة العرب السنة وفقا للعرف السياسي الدارج منذ تشكيل النظام السياسي العراقي بعد عام 2003، في حين يذهب منصبا رئيس الوزراء ورئيس الجمهورية للشيعة والأكراد بالترتيب."
  ],
  "image": "http://img.parlmany.com/large/202312181049304930.jpg",
  "favicon": "https://www.parlmany.com/styleImages/logoIco.jpg",
  "domain": "www.parlmany.com",
  "url": "http://www.parlmany.com/News/5/547649/السبت-المقبل-البرلمان-العراقي-يقرر-عقد-جلسة-لانتخاب-رئيس-جديد",
  "date": "2024-05-13T20:00:00Z"
}
```
