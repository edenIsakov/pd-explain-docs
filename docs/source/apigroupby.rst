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

    Compute count of groups, excluding missing values.
    Add the operation "groupby" to the result object.

    :return: Count for each group.

.. method:: mean(
        numeric_only: bool | lib.NoDefault = lib.no_default,
        engine: str = "cython",
        engine_kwargs: dict[str, bool] | None = None
    )

    Compute mean of groups, excluding missing values.
    Add the operation "groupby" to the result object.

    :param numeric_only: Include only float, int, boolean columns.
                         If None, will attempt to use everything, then use only numeric data.
    :param engine: * 'cython' : Runs the operation through C-extensions from cython.
                   * 'numba' : Runs the operation through JIT compiled code from numba.
                   * None : Defaults to 'cython' or globally setting compute.use_numba.
    :param engine_kwargs: * For 'cython' engine, there are no accepted engine_kwargs.
                          * For 'numba' engine, the engine can accept nopython, nogil, and parallel dictionary keys.
                            The values must either be True or False.
                            The default engine_kwargs for the 'numba' engine is
                            {'nopython': True, 'nogil': False, 'parallel': False}.
    :return: Mean value for each group.

.. method:: median(numeric_only: bool | lib.NoDefault = lib.no_default)

    Compute median of groups, excluding missing values.
    Add the operation "groupby" to the result object.

    :param numeric_only: Include only float, int, boolean columns.
                         If None, will attempt to use everything, then use only numeric data.
    :return: Median of values within each group.

.. method:: sum(
        numeric_only: bool | lib.NoDefault = lib.no_default,
        min_count: int = 0,
        engine: str | None = None,
        engine_kwargs: dict[str, bool] | None = None
    )

    Compute sum of group values.
    Add the operation "groupby" to the result object.

    :param numeric_only: Include only float, int, boolean columns.
                         If None, will attempt to use everything, then use only numeric data.
    :param min_count: The required number of valid values to perform the operation.
                      If fewer than min_count non-NA values are present, the result will be NA.
    :param engine: * 'cython' : Runs the operation through C-extensions from cython.
                   * 'numba' : Runs the operation through JIT compiled code from numba.
                   * None : Defaults to 'cython' or globally setting compute.use_numba.
    :param engine_kwargs: * For 'cython' engine, there are no accepted engine_kwargs.
                          * For 'numba' engine, the engine can accept nopython, nogil, and parallel dictionary keys.
                            The values must either be True or False.
                            The default engine_kwargs for the 'numba' engine is
                            {'nopython': True, 'nogil': False, 'parallel': False}.
    :return: Computed sum of values within each group.

.. method:: min(numeric_only: bool = False, min_count: int = -1)

    Compute min of group values.
    Add the operation "groupby" to the result object.

    :param numeric_only: Include only float, int, boolean columns.
                         If None, will attempt to use everything, then use only numeric data.
    :param min_count: The required number of valid values to perform the operation.
                      If fewer than min_count non-NA values are present, the result will be NA.
    :return: Computed min of values within each group.

.. method:: max(numeric_only: bool = False, min_count: int = -1)

    Compute max of group values.
    Add the operation "groupby" to the result object.

    :param numeric_only: Include only float, int, boolean columns.
                         If None, will attempt to use everything, then use only numeric data.
    :param min_count: The required number of valid values to perform the operation.
                      If fewer than min_count non-NA values are present, the result will be NA.
    :return: Computed max of values within each group.
