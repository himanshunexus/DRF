# Validation report

Actual local execution results; not a claim that videos were watched.

Python: 3.14.8

- Django: 5.2.19
- djangorestframework: 3.16.1
- django-filter: 25.2
- djangorestframework-simplejwt: 5.5.1

Each project ran in a separate process. Checks: generate migration, Django system check, migrate SQLite, seed data, tests, migration drift check.

| Project | Result | Tests |
|---|---|---:|
| [01_what_is_api](01_what_is_api/README.md) | PASS | 1 |
| [02_what_is_web_api](02_what_is_web_api/README.md) | PASS | 1 |
| [03_rest_and_rest_api](03_rest_and_rest_api/README.md) | PASS | 1 |
| [04_install_drf](04_install_drf/README.md) | PASS | 1 |
| [05_study_material](05_study_material/README.md) | PASS | 1 |
| [06_serialization](06_serialization/README.md) | PASS | 1 |
| [07_serializer_fields](07_serializer_fields/README.md) | PASS | 5 |
| [08_deserialization](08_deserialization/README.md) | PASS | 4 |
| [09_django_crud_fbv_cbv](09_django_crud_fbv_cbv/README.md) | PASS | 4 |
| [10_validation](10_validation/README.md) | PASS | 4 |
| [11_model_serializer](11_model_serializer/README.md) | PASS | 3 |
| [12_function_based_api_view](12_function_based_api_view/README.md) | PASS | 2 |
| [13_class_based_api_view](13_class_based_api_view/README.md) | PASS | 2 |
| [14_generics_and_mixins](14_generics_and_mixins/README.md) | PASS | 3 |
| [15_concrete_views](15_concrete_views/README.md) | PASS | 3 |
| [16_viewset](16_viewset/README.md) | PASS | 2 |
| [17_model_viewset](17_model_viewset/README.md) | PASS | 3 |
| [18_basic_authentication](18_basic_authentication/README.md) | PASS | 5 |
| [19_session_authentication](19_session_authentication/README.md) | PASS | 4 |
| [20_custom_permissions](20_custom_permissions/README.md) | PASS | 3 |
| [21_function_view_authentication](21_function_view_authentication/README.md) | PASS | 3 |
| [22_token_authentication](22_token_authentication/README.md) | PASS | 4 |
| [23_custom_authentication](23_custom_authentication/README.md) | PASS | 5 |
| [24_simple_jwt](24_simple_jwt/README.md) | PASS | 5 |
| [25_throttling](25_throttling/README.md) | PASS | 2 |
| [26_filtering](26_filtering/README.md) | PASS | 3 |
| [27_search_filter](27_search_filter/README.md) | PASS | 3 |
| [28_ordering_filter](28_ordering_filter/README.md) | PASS | 3 |
| [29_page_number_pagination](29_page_number_pagination/README.md) | PASS | 4 |
| [30_limit_offset_pagination](30_limit_offset_pagination/README.md) | PASS | 4 |
| [31_cursor_pagination](31_cursor_pagination/README.md) | PASS | 4 |
| [32_serializer_relations](32_serializer_relations/README.md) | PASS | 4 |
| [33_hyperlinked_serializer](33_hyperlinked_serializer/README.md) | PASS | 3 |
| [34_nested_serializer](34_nested_serializer/README.md) | PASS | 4 |
| [35_final_api_project](35_final_api_project/README.md) | PASS | 8 |

Total: 35/35 projects passed; 112 tests executed.

Full command output: [validation_results.json](validation_results.json).

Limits: tested on the interpreter above; other Python versions were not run. These are in-process HTTP tests. The separate sampled lecture review is documented in RESEARCH.md. Production deployment/security auditing was not performed.
