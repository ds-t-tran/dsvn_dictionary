from django.db import models

# Create your models here.

class DsvnDictionary(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Vi_Dictionary(models.Model):
    vi_text = models.CharField(max_length=200, blank=False, default='')
    kanji_text = models.CharField(max_length=200, blank=True, default='')
    hiragana_text = models.CharField(max_length=200, blank=True, default='')
    katakana_text = models.CharField(max_length=200, blank=True, default='')
    eng_text = models.CharField(max_length=200, blank=True, default='')
    example = models.CharField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.vi_text
    
    class Meta:
        db_table = 'dsvn_dictionary_vi_dictionary'

class Ja_Dictionary(models.Model):
    hiragana_text = models.CharField(max_length=200, blank=True, default='')
    kanji_text = models.CharField(max_length=200, blank=True, default='')
    katakana_text = models.CharField(max_length=200, blank=True, default='')
    vi_text = models.CharField(max_length=200, blank=True, default='')
    eng_text = models.CharField(max_length=200, blank=True, default='')
    example = models.CharField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hiragana_text

    class Meta:
        db_table = 'dsvn_dictionary_ja_dictionary'
