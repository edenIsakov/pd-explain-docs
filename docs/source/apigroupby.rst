.. _exp_dataframe_groupby:

=============================================
ExpDataFrameGroupBy Class API
=============================================

Overview
--------

`ExpDataFrameGroupBy` is a specialized class that extends the functionality of the pd-explain ExpDataFrame class. It is designed to provide additional capabilities for explaining grouped data operations applied to DataFrames, making it easier to understand and work with grouped data transformations.

.. inheritance-diagram:: ExpDataFrameGroupBy
   :parts: 1

Methods
-------

.. method:: count()

    :return: Count for each group.

.. method:: mean(numeric_only=lib.no_default, engine="cython", engine_kwargs=None)
   
    Compute mean of groups, excluding missing values.
    
    :param numeric_only: Include only float, int, boolean columns.
    :type numeric_only: bool, optional
    :param engine: Engine for computation.
    :type engine: str, optional
    :param engine_kwargs: Engine-specific keyword arguments.
    :type engine_kwargs: dict[str, bool], optional
    :return: Mean value for each group.

.. method:: median(numeric_only=lib.no_default)

    Compute median of groups, excluding missing values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool | lib.NoDefault
    :return: Median of values within each group.

.. method:: sum(numeric_only=lib.no_default, min_count=0, engine=None, engine_kwargs=None)

    Compute sum of group values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool | lib.NoDefault
    :param min_count: Optional. The required number of valid values to perform the operation.
    :type min_count: int
    :param engine: Optional. Engine for computation.
    :type engine: str | None
    :param engine_kwargs: Optional. Engine-specific keyword arguments.
    :type engine_kwargs: dict[str, bool] | None
    :return: Computed sum of values within each group.

.. method:: min(numeric_only=False, min_count=-1)

    Compute min of group values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool
    :param min_count: Optional. The required number of valid values to perform the operation.
    :type min_count: int
    :return: Computed min of values within each group.

.. method:: max(numeric_only=False, min_count=-1)

    Compute max of group values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool
    :param min_count: Optional. The required number of valid values to perform the operation.
    :type min_count: int
    :return: Computed max of values within each group.
