// Copyright (C) 2023 Intel Corporation
// SPDX-License-Identifier: Apache-2.0
//

#pragma once

#include <cstddef>
#include <cstdint>

namespace ov {
namespace intel_gna {
namespace pre_post_processing {

class HwAcceleratedDataConverter {
public:
    /**
     * @brief Convert 2D matrix of fp32 to int16 using hardware acceleration. Rounding and integer overflow are taken
     * into account. Zero-padding is not supported.
     */
    virtual void convert_matrix_fp32_to_int16_no_zero_padding(int16_t* ptr_dst,
                                                              const float* ptr_src,
                                                              const size_t num_rows,
                                                              const size_t num_columns,
                                                              const float scale_factor,
                                                              bool transpose) const = 0;
    /**
     * @brief Convert 2D matrix of fp32 to int8 using hardware acceleration. Rounding and integer overflow are taken
     * into account. Zero-padding is not supported.
     */
    virtual void convert_matrix_fp32_to_int8_no_zero_padding(int8_t* ptr_dst,
                                                             const float* ptr_src,
                                                             const size_t num_rows,
                                                             const size_t num_columns,
                                                             const float scale_factor,
                                                             bool transpose) const = 0;
    /**
     * @brief Convert 2D matrix of int32 to fp32 using hardware acceleration. Zero-padding is not supported.
     */
    virtual void convert_matrix_int32_to_fp32_no_zero_padding(float* ptr_dst,
                                                              const int32_t* ptr_src,
                                                              size_t num_rows,
                                                              size_t num_columns,
                                                              float scale_factor,
                                                              bool transpose) const = 0;
    /**
     * @brief Convert 2D matrix of int16 to fp32 using hardware acceleration. Zero-padding is not supported.
     */
    virtual void convert_matrix_int16_to_fp32_no_zero_padding(float* ptr_dst,
                                                              const int16_t* ptr_src,
                                                              size_t num_rows,
                                                              size_t num_columns,
                                                              float scale_factor,
                                                              bool transpose) const = 0;
    /**
     * @brief Convert 2D matrix of int8 to fp32 using hardware acceleration. Zero-padding is not supported.
     */
    virtual void convert_matrix_int8_to_fp32_no_zero_padding(float* ptr_dst,
                                                             const int8_t* ptr_src,
                                                             size_t num_rows,
                                                             size_t num_columns,
                                                             float scale_factor,
                                                             bool transpose) const = 0;
};
}  // namespace pre_post_processing
}  // namespace intel_gna
}  // namespace ov