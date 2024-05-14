> DOCUMENTATION

## /gnews Endpoint

This endpoint allows you to retrieve the newest top news related to a specific search term from Google News.

### Request

**Method:** `GET`

**URL:** `https://goopi.thepolygon.xyz/gnews`

**Query Parameters:**

- `query`: (required) The search term for Google News.
- `lang`: (optional) Language code (ar or en), defaults to `ar`.
- `region`: (optional) Region code (US or IQ), defaults to `IQ`.
- `period`: (optional) [int]s, [int]h, [int]d, [int]w, [int]m, [int]y.

**Authorization:**

- `Bearer Token`: (required) Bearer `<Your API key>
`

### Example

> **GET** https://goopi.thepolygon.xyz/gnews?query=Iraqi speaker

**Response:**

```json
[
  {
    "title": "السبت المقبل .. البرلمان العراقي يقرر عقد جلسة لانتخاب رئيس جديد",
    "desc": null,
    "date": "12 hours ago",
    "datetime": "2024-05-13T21:38:32.162562",
    "link": "news.google.com/articles/CBMi6AJodHRwczovL3d3dy5wY...",
    "media": "برلمانى",
    "site": null,
    "reporter": null
  }
]
```

---

## /goose Endpoint

This endpoint extracts data from a given Google News URL.

### Request

**Method:** `GET`
**URL:** `https://goopi.thepolygon.xyz/goose`
**Query Parameters:**

- `gnews_url`: (required) The URL of the Google News article to extract data from.

**Authorization:**

- `Bearer Token`: (required) Bearer `<Your API key>

### Example

> **GET** https://goopi.thepolygon.xyz/goose?gnews_url=news.google.com/articles/article123

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
