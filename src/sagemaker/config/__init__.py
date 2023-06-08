# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying athis file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""This module configures the default values for SageMaker Python SDK."""

from __future__ import absolute_import
from sagemaker.config.config import load_sagemaker_config, validate_sagemaker_config  # noqa: F401
from sagemaker.config.config_schema import (  # noqa: F401
    KEY,
    TRAINING_JOB,
    TRAINING_JOB_INTER_CONTAINER_ENCRYPTION_PATH,
    TRAINING_JOB_ROLE_ARN_PATH,
    TRAINING_JOB_ENABLE_NETWORK_ISOLATION_PATH,
    TRAINING_JOB_ENVIRONMENT_PATH,
    TRAINING_JOB_VPC_CONFIG_PATH,
    TRAINING_JOB_OUTPUT_DATA_CONFIG_PATH,
    TRAINING_JOB_RESOURCE_CONFIG_PATH,
    PROCESSING_JOB_INPUTS_PATH,
    PROCESSING_JOB,
    PROCESSING_JOB_ENVIRONMENT_PATH,
    PROCESSING_JOB_INTER_CONTAINER_ENCRYPTION_PATH,
    PROCESSING_JOB_ROLE_ARN_PATH,
    PROCESSING_JOB_NETWORK_CONFIG_PATH,
    PROCESSING_OUTPUT_CONFIG_PATH,
    PROCESSING_JOB_PROCESSING_RESOURCES_PATH,
    MONITORING_JOB_ENVIRONMENT_PATH,
    MONITORING_JOB_ROLE_ARN_PATH,
    MONITORING_JOB_VOLUME_KMS_KEY_ID_PATH,
    MONITORING_JOB_NETWORK_CONFIG_PATH,
    MONITORING_JOB_OUTPUT_KMS_KEY_ID_PATH,
    MONITORING_SCHEDULE,
    MONITORING_SCHEDULE_INTER_CONTAINER_ENCRYPTION_PATH,
    AUTO_ML_ROLE_ARN_PATH,
    AUTO_ML_OUTPUT_CONFIG_PATH,
    AUTO_ML_JOB_CONFIG_PATH,
    AUTO_ML_JOB,
    COMPILATION_JOB_ROLE_ARN_PATH,
    COMPILATION_JOB_OUTPUT_CONFIG_PATH,
    COMPILATION_JOB_VPC_CONFIG_PATH,
    COMPILATION_JOB,
    EDGE_PACKAGING_ROLE_ARN_PATH,
    EDGE_PACKAGING_OUTPUT_CONFIG_PATH,
    EDGE_PACKAGING_JOB,
    TRANSFORM_JOB,
    TRANSFORM_JOB_KMS_KEY_ID_PATH,
    TRANSFORM_OUTPUT_KMS_KEY_ID_PATH,
    VOLUME_KMS_KEY_ID,
    TRANSFORM_JOB_VOLUME_KMS_KEY_ID_PATH,
    MODEL,
    MODEL_CONTAINERS_PATH,
    MODEL_EXECUTION_ROLE_ARN_PATH,
    MODEL_ENABLE_NETWORK_ISOLATION_PATH,
    MODEL_VPC_CONFIG_PATH,
    MODEL_PACKAGE_VALIDATION_ROLE_PATH,
    VALIDATION_ROLE,
    VALIDATION_PROFILES,
    MODEL_PACKAGE_INFERENCE_SPECIFICATION_CONTAINERS_PATH,
    MODEL_PACKAGE_VALIDATION_PROFILES_PATH,
    MODEL_PRIMARY_CONTAINER_PATH,
    MODEL_PRIMARY_CONTAINER_ENVIRONMENT_PATH,
    ENDPOINT_CONFIG_PRODUCTION_VARIANTS_PATH,
    KMS_KEY_ID,
    ENDPOINT_CONFIG_KMS_KEY_ID_PATH,
    ENDPOINT_CONFIG,
    ENDPOINT_CONFIG_DATA_CAPTURE_PATH,
    ENDPOINT_CONFIG_ASYNC_INFERENCE_PATH,
    SAGEMAKER,
    FEATURE_GROUP,
    TAGS,
    FEATURE_GROUP_ROLE_ARN_PATH,
    FEATURE_GROUP_ONLINE_STORE_CONFIG_PATH,
    FEATURE_GROUP_OFFLINE_STORE_CONFIG_PATH,
    PIPELINE_ROLE_ARN_PATH,
    TRANSFORM_RESOURCES_VOLUME_KMS_KEY_ID_PATH,
    EDGE_PACKAGING_KMS_KEY_ID_PATH,
    ENDPOINT_CONFIG_ASYNC_KMS_KEY_ID_PATH,
    PROCESSING_JOB_KMS_KEY_ID_PATH,
    PROCESSING_JOB_SECURITY_GROUP_IDS_PATH,
    PROCESSING_JOB_SUBNETS_PATH,
    PROCESSING_JOB_ENABLE_NETWORK_ISOLATION_PATH,
    PROCESSING_JOB_VOLUME_KMS_KEY_ID_PATH,
    PIPELINE_TAGS_PATH,
    TRAINING_JOB_VOLUME_KMS_KEY_ID_PATH,
    TRAINING_JOB_SECURITY_GROUP_IDS_PATH,
    TRAINING_JOB_SUBNETS_PATH,
    TRAINING_JOB_KMS_KEY_ID_PATH,
    FEATURE_GROUP_OFFLINE_STORE_KMS_KEY_ID_PATH,
    FEATURE_GROUP_ONLINE_STORE_KMS_KEY_ID_PATH,
    AUTO_ML_KMS_KEY_ID_PATH,
    AUTO_ML_VPC_CONFIG_PATH,
    AUTO_ML_VOLUME_KMS_KEY_ID_PATH,
    AUTO_ML_INTER_CONTAINER_ENCRYPTION_PATH,
    ENDPOINT_CONFIG_DATA_CAPTURE_KMS_KEY_ID_PATH,
    SESSION_DEFAULT_S3_BUCKET_PATH,
    SESSION_DEFAULT_S3_OBJECT_KEY_PREFIX_PATH,
    MONITORING_SCHEDULE_CONFIG,
    MONITORING_JOB_DEFINITION,
    MONITORING_OUTPUT_CONFIG,
    MONITORING_RESOURCES,
    CLUSTER_CONFIG,
    NETWORK_CONFIG,
    ENABLE_INTER_CONTAINER_TRAFFIC_ENCRYPTION,
    ENABLE_NETWORK_ISOLATION,
    VPC_CONFIG,
    SUBNETS,
    SECURITY_GROUP_IDS,
    ROLE_ARN,
    VALUE,
    OUTPUT_CONFIG,
    DATA_CAPTURE_CONFIG,
    PRODUCTION_VARIANTS,
    AUTO_ML_JOB_CONFIG,
    SECURITY_CONFIG,
    OUTPUT_DATA_CONFIG,
    MODEL_PACKAGE,
    VALIDATION_SPECIFICATION,
    TRANSFORM_JOB_DEFINITION,
    TRANSFORM_JOB_ENVIRONMENT_PATH,
    TRANSFORM_OUTPUT,
    TRANSFORM_RESOURCES,
    OFFLINE_STORE_CONFIG,
    S3_STORAGE_CONFIG,
    ONLINE_STORE_CONFIG,
    PROCESSING_INPUTS,
    DATASET_DEFINITION,
    ATHENA_DATASET_DEFINITION,
    REDSHIFT_DATASET_DEFINITION,
    CLUSTER_ROLE_ARN,
    PROCESSING_OUTPUT_CONFIG,
    PROCESSING_RESOURCES,
    RESOURCE_CONFIG,
    EXECUTION_ROLE_ARN,
    ASYNC_INFERENCE_CONFIG,
    SCHEMA_VERSION,
    PYTHON_SDK,
    MODULES,
    DEFAULT_S3_BUCKET,
    DEFAULT_S3_OBJECT_KEY_PREFIX,
    SESSION,
    ENVIRONMENT,
    CONTAINERS,
    PRIMARY_CONTAINER,
    INFERENCE_SPECIFICATION,
)
