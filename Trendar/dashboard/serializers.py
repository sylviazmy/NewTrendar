# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import in_textrank,in_extract_tags,negative,sentiment,neg_total


class T_ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = in_textrank
        fields = ('name', 'rank')

class E_ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = in_extract_tags
        fields = ('name', 'rank')

class NegativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = negative
        fields = ('typeof', 'score', 'content')

class NegativeRecourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = negative
        fields = ('content',)

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = sentiment
        fields = ('number',)

class NegTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = neg_total
        fields = ('typeof','number')