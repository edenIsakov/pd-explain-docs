.. _exp_dataframe_groupby:

=============================================
ExpDataFrameGroupBy Class API
=============================================

Overview
--------

`ExpDataFrameGroupBy` is a specialized class that extends the functionality of the pandas DataFrameGroupBy class. It is designed to provide additional capabilities for explaining grouped data operations applied to DataFrames, making it easier to understand and work with grouped data transformations.

.. inheritance-diagram:: ExpDataFrameGroupBy
   :parts: 1

Methods
-------

.. method:: count()

    :return: Count for each group.

.. method:: mean(numeric_only: bool | lib.NoDefault = lib.no_default, engine: str = "cython", engine_kwargs: dict[str, bool] | None = None)
   
   Compute mean of groups, excluding missing values.
    
    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool | lib.NoDefault
    :param engine: Optional. Engine for computation.
    :type engine: str
    :param engine_kwargs: Optional. Engine-specific keyword arguments.
    :type engine_kwargs: dict[str, bool] | None
    :return: Mean value for each group.

.. method:: median(numeric_only: bool | lib.NoDefault = lib.no_default)

   Compute median of groups, excluding missing values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool | lib.NoDefault
    :return: Median of values within each group.

.. method:: sum(numeric_only: bool | lib.NoDefault = lib.no_default, min_count: int = 0, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None)

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

.. method:: min(numeric_only: bool = False, min_count: int = -1)

   Compute min of group values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool
    :param min_count: Optional. The required number of valid values to perform the operation.
    :type min_count: int
    :return: Computed min of values within each group.

.. method:: max(numeric_only: bool = False, min_count: int = -1)

   Compute max of group values.

    :param numeric_only: Optional. Include only float, int, boolean columns.
    :type numeric_only: bool
    :param min_count: Optional. The required number of valid values to perform the operation.
    :type min_count: int
    :return: Computed max of values within each group.
