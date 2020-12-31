from __future__ import unicode_literals
from hazm import *

normalizer = Normalizer()

print(normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند'))


print(sent_tokenize('ما هم برای وصل کردن آمدیم! ولی برای پردازش، جدا بهتر نیست؟'))

#['ما هم برای وصل کردن آمدیم!', 'ولی برای پردازش، جدا بهتر نیست؟']
print(word_tokenize('ولی برای پردازش، جدا بهتر نیست؟'))
print("salam")
#['ولی', 'برای', 'پردازش', '،', 'جدا', 'بهتر', 'نیست', '؟']

stemmer = Stemmer()
print(stemmer.stem('کتاب‌ها'))
#'کتاب'
lemmatizer = Lemmatizer()

print(lemmatizer.lemmatize('می‌روم'))
#'رفت#رو'
exit(0)
tagger = POSTagger(model='resources/postagger.model')
tagger.tag(word_tokenize('ما بسیار کتاب می‌خوانیم'))
#[('ما', 'PRO'), ('بسیار', 'ADV'), ('کتاب', 'N'), ('می‌خوانیم', 'V')]

chunker = Chunker(model='resources/chunker.model')
tagged = tagger.tag(word_tokenize('کتاب خواندن را دوست داریم'))
tree2brackets(chunker.parse(tagged))
#'[کتاب خواندن NP] [را POSTP] [دوست داریم VP]'

parser = DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
parser.parse(word_tokenize('زنگ‌ها برای که به صدا درمی‌آید؟'))

