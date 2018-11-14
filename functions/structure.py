from functions import measures as msrs
import numpy as np


class Structure_of_measures:
    def __init__(self):
        self.mean = []
        self.median = []
        self.r = []
        self.trimmed = []
        self.q = []
        self.sq = []
        self.ab = []
        self.range = []
        self.iqr = []
        self.mad = []

    def __add__(self, other):
        self.mean.append(msrs.sample_mean(other))
        self.median.append(msrs.sample_median(other))
        self.r.append(msrs.sample_r(other))
        self.trimmed.append(msrs.trimmed_mean(other))
        self.q.append(msrs.sample_q(other))
        self.sq.append(msrs.sq_deviation(other))
        self.ab.append(msrs.ab_deviation(other))
        self.range.append(msrs.sample_range(other))
        self.iqr.append(msrs.iqr(other))
        self.mad.append(msrs.mad(other))

    def calc_var(self):
        list_of_measures = []
        list_of_measures.append(msrs.sample_mean(np.power(self.mean, 2))-msrs.sample_mean(self.mean)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.median, 2))-msrs.sample_mean(self.median)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.r, 2))-msrs.sample_mean(self.r)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.trimmed, 2))-msrs.sample_mean(self.trimmed)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.q, 2))-msrs.sample_mean(self.q)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.sq, 2)) - msrs.sample_mean(self.sq)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.ab, 2)) - msrs.sample_mean(self.ab)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.range, 2)) - msrs.sample_mean(self.range)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.iqr, 2)) - msrs.sample_mean(self.iqr)**2)
        list_of_measures.append(msrs.sample_mean(np.power(self.mad, 2)) - msrs.sample_mean(self.mad)**2)
        return list_of_measures

    def calc_mean(self):
        list_of_measures = []
        list_of_measures.append(msrs.sample_mean(self.mean))
        list_of_measures.append(msrs.sample_mean(self.median))
        list_of_measures.append(msrs.sample_mean(self.r))
        list_of_measures.append(msrs.sample_mean(self.trimmed))
        list_of_measures.append(msrs.sample_mean(self.q))
        list_of_measures.append(msrs.sample_mean(self.sq))
        list_of_measures.append(msrs.sample_mean(self.ab))
        list_of_measures.append(msrs.sample_mean(self.range))
        list_of_measures.append(msrs.sample_mean(self.iqr))
        list_of_measures.append(msrs.sample_mean(self.mad))
        return list_of_measures

