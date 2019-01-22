# coding: utf-8

# flake8: noqa

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.59"

# import apis into sdk package
from criteo_marketing.api.advertisers_api import AdvertisersApi
from criteo_marketing.api.audiences_api import AudiencesApi
from criteo_marketing.api.authentication_api import AuthenticationApi
from criteo_marketing.api.budgets_api import BudgetsApi
from criteo_marketing.api.campaigns_api import CampaignsApi
from criteo_marketing.api.categories_api import CategoriesApi
from criteo_marketing.api.portfolio_api import PortfolioApi
from criteo_marketing.api.publishers_api import PublishersApi
from criteo_marketing.api.sellers_api import SellersApi
from criteo_marketing.api.statistics_api import StatisticsApi

# import ApiClient
from criteo_marketing.api_client import ApiClient
from criteo_marketing.configuration import Configuration
# import models into sdk package
from criteo_marketing.models.audience_create_request import AudienceCreateRequest
from criteo_marketing.models.audience_create_response import AudienceCreateResponse
from criteo_marketing.models.audience_patch_request import AudiencePatchRequest
from criteo_marketing.models.audience_patch_response import AudiencePatchResponse
from criteo_marketing.models.audience_put_request import AudiencePutRequest
from criteo_marketing.models.audience_response import AudienceResponse
from criteo_marketing.models.audiences_get_response import AudiencesGetResponse
from criteo_marketing.models.bid_message import BidMessage
from criteo_marketing.models.budget_message import BudgetMessage
from criteo_marketing.models.campaign_bid_change_request import CampaignBidChangeRequest
from criteo_marketing.models.campaign_bid_change_response import CampaignBidChangeResponse
from criteo_marketing.models.campaign_bid_message import CampaignBidMessage
from criteo_marketing.models.campaign_message import CampaignMessage
from criteo_marketing.models.category_bid_change_request import CategoryBidChangeRequest
from criteo_marketing.models.category_bid_message import CategoryBidMessage
from criteo_marketing.models.category_message import CategoryMessage
from criteo_marketing.models.category_update_error import CategoryUpdateError
from criteo_marketing.models.category_update_input import CategoryUpdateInput
from criteo_marketing.models.category_updates_per_catalog import CategoryUpdatesPerCatalog
from criteo_marketing.models.category_updates_per_catalog_error import CategoryUpdatesPerCatalogError
from criteo_marketing.models.check_result import CheckResult
from criteo_marketing.models.client_registration_request_message import ClientRegistrationRequestMessage
from criteo_marketing.models.client_registration_response_message import ClientRegistrationResponseMessage
from criteo_marketing.models.i_throttling_configuration import IThrottlingConfiguration
from criteo_marketing.models.inline_response200 import InlineResponse200
from criteo_marketing.models.mapi_user_message import MapiUserMessage
from criteo_marketing.models.message_with_details_campaign_bid_change_response import MessageWithDetailsCampaignBidChangeResponse
from criteo_marketing.models.message_with_details_category_updates_per_catalog_error import MessageWithDetailsCategoryUpdatesPerCatalogError
from criteo_marketing.models.policy_route_info import PolicyRouteInfo
from criteo_marketing.models.portfolio_message import PortfolioMessage
from criteo_marketing.models.publisher_file_stats_message import PublisherFileStatsMessage
from criteo_marketing.models.publisher_stats_message import PublisherStatsMessage
from criteo_marketing.models.publisher_stats_query_message import PublisherStatsQueryMessage
from criteo_marketing.models.route_policy import RoutePolicy
from criteo_marketing.models.seller_bid_info_message import SellerBidInfoMessage
from criteo_marketing.models.seller_bids_message import SellerBidsMessage
from criteo_marketing.models.seller_budget_create_message import SellerBudgetCreateMessage
from criteo_marketing.models.seller_budget_info_message import SellerBudgetInfoMessage
from criteo_marketing.models.seller_budget_response_message import SellerBudgetResponseMessage
from criteo_marketing.models.seller_budget_update_message import SellerBudgetUpdateMessage
from criteo_marketing.models.seller_budgets_create_message import SellerBudgetsCreateMessage
from criteo_marketing.models.seller_budgets_message import SellerBudgetsMessage
from criteo_marketing.models.seller_budgets_update_message import SellerBudgetsUpdateMessage
from criteo_marketing.models.seller_campaign_message import SellerCampaignMessage
from criteo_marketing.models.seller_info_message import SellerInfoMessage
from criteo_marketing.models.seller_message import SellerMessage
from criteo_marketing.models.service_status_check_result import ServiceStatusCheckResult
from criteo_marketing.models.stats_query_message import StatsQueryMessage
from criteo_marketing.models.stats_query_message_ex import StatsQueryMessageEx
from criteo_marketing.models.throttle_policy import ThrottlePolicy
from criteo_marketing.models.throttle_policy_rates import ThrottlePolicyRates
