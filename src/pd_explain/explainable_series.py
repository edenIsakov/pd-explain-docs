from __future__ import annotations

from typing import List

import pandas as pd
from pandas._typing import Dtype
from subtab.SubTub import SubTub


class ExpSeries(pd.Series):
    """
    Explainable series, Inherit from pandas Series.
    """

    def __init__(
            self,
            data=None,
            index=None,
            dtype: Dtype | None = None,
            name=None,
            copy: bool = False,
            fastpath: bool = False,
            calc_subtab: bool = False,
            use_rules: bool = False,
            subtub_config: dict = {}
    ):
        """
        Initialize new explain series

        :param data: Contains data stored in Series. If data is a dict, argument order is maintained.
        :param index: Values must be hashable and have the same length as data. Non-unique index values are allowed.
                      Will default to RangeIndex (0, 1, 2, …, n) if not provided.
                      If data is dict-like and index is None, then the keys in the data are used as the index.
                      If the index is not None, the resulting Series is reindexed with the index values.
        :param dtype: Data type for the output Series. If not specified, this will be inferred from data.
        :param name: The name to give to the Series.
        :param copy: Copy input data. Only affects Series or 1d ndarray input. See examples.
        :param fastpath:
        :param calc_subtab: Calculate sub table for the dataframe
        :param use_rules: Whethere use rules in the subtab calculation or not
        :param subtub_config: config for subtab calculation
        """
        super().__init__(data, index, dtype, name, copy, fastpath)
        self.explanation = None
        self.operation = None
        self.filter_items = []
        if calc_subtab:
            self.subtab = SubTub(self, use_rules, subtub_config)

    def explain(self, schema: dict = None, attributes: List = None, top_k: int = 1, figs_in_row: int = 2,
                show_scores: bool = False):
        """
        Generate explanation to series base on the operation lead to this series result

        :param schema: result columns, can change columns name and ignored columns
        :param attributes: list of specific columns to consider in the explanation
        :param top_k: number of explanations
        :param figs_in_row: number of explanations figs in one row
        :param show_scores: show scores on explanation

        :return: explanation figures
        """
        if attributes is None:
            attributes = []

        if schema is None:
            schema = {}

        return self.operation.explain(schema=schema, attributes=attributes, top_k=top_k,
                                      figs_in_row=figs_in_row, show_scores=show_scores)

    def calc_subtab(self, use_rules: bool = False, subtub_config: dict = {}):
        """
        Calculate subtab for this dataframe
        """
        if not self.subtab:
            from pd_explain.utils import pandas_read, _read
            pd.io.parsers.readers._read = pandas_read
            self.subtab = SubTub(self, use_rules, subtub_config)
            pd.io.parsers.readers._read = _read

    def display(self):
        """
        display dataframe subtab
        """
        if not self.subtab:
            self.calc_subtab()

        self.subtab.display(self)
