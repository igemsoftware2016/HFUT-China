# -*- coding:utf-8 -*-
from django.shortcuts import render
from projectManage.models import *
from accounts.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from utils.functionTools.generalFunction import noneIfEmptyString,noneIfNoKey,myError
import json
import string


# Create your views here.

def searchGenes(request):
	try:
		data = json.loads(request.body)
		try:
			token = Token.objects.filter(token=data['token']).first()
			user = token.user
		except:
			raise myError('Please Log In.')
		keyword = data['keyword']
		search_result = search_genes(keyword)
		result = {
			'successful': True,
			'data': search_result,
			'error': {
				'id': '',
				'msg': '',
			},
		}
	except myError, e:
		result = {
			'successful': False,
			'error': {
				'id': '3',
				'msg': e.value,
			}
		}
	except Exception,e:
		result = {
			'successful': False,
			'error': {
				'id': '1024',
				'msg': e.args
			}
		}
	finally:
		return HttpResponse(json.dumps(result), content_type='application/json')


def getGeneInfo(request):
	try:
		data = json.loads(request.body)
		try:
			token = Token.objects.filter(token=data['token']).first()
			user = token.user
		except:
			raise myError('Please Log In.')
		gene_id = data['gene_id']
		get_result = get_gene_info(gene_id)
		result = {
			'successful': get_result[0],
			'data': get_result[1],
			'error': {
				'id': '',
				'msg': '',
			},
		}
	except myError, e:
		result = {
			'successful': False,
			'error': {
				'id': '3',
				'msg': e.value,
			}
		}
	except Exception,e:
		result = {
			'successful': False,
			'error': {
				'id': '1024',
				'msg': e.args
			}
		}
	finally:
		return HttpResponse(json.dumps(result), content_type='application/json')

def getRelatedGene(request):
	try:
		data = json.loads(request.body)
		try:
			token = Token.objects.filter(token=data['token']).first()
			user = token.user
		except:
			raise myError('Please Log In.')
		gene_name = data['gene_name']
		realated_gene_list = []
		realated_genes = search_realated_genes(gene_name)
		result = {
			'successful': True,
			'data': graph_result,
			'error': {
				'id': '',
				'msg': '',
			},
		}
	except myError, e:
		result = {
			'successful': False,
			'error': {
				'id': '3',
				'msg': e.value,
			}
		}
	except Exception,e:
		result = {
			'successful': False,
			'error': {
				'id': '1024',
				'msg': e.args
			}
		}
	finally:
		return HttpResponse(json.dumps(result), content_type='application/json')