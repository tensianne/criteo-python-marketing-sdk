# Criteo Marketing SDK for Python
[![Build Status](https://travis-ci.com/criteo/criteo-python-marketing-sdk.svg?branch=master)](https://travis-ci.com/criteo/criteo-python-marketing-sdk)
[![](https://img.shields.io/pypi/pyversions/criteo-marketing.svg)](https://pypi.org/project/criteo-marketing/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v.1.0
- Package version: 1.0.167

## Requirements.

Python 2.7 and 3.5+

## Installation & Usage
### pip install


```sh
pip install criteo_marketing
```
(you may need to run `pip` with root permission: `sudo pip install criteo_marketing`)

Then import the package:
```python
import criteo_marketing 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import criteo_marketing
```

## Example
Please see [examples/](examples/) for full examples to get a valid token and make a call to the API.

## Documentation for API Endpoints

All URIs are relative to *https://api.criteo.com/marketing*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvertisersApi* | [**get_campaigns**](docs/AdvertisersApi.md#get_campaigns) | **GET** /v1/advertisers/{advertiserId}/campaigns | Gets all advertiser&#39;s campaigns
*AdvertisersApi* | [**get_categories**](docs/AdvertisersApi.md#get_categories) | **GET** /v1/advertisers/{advertiserId}/categories | Gets all advertiser&#39;s categories
*AdvertisersApi* | [**get_category**](docs/AdvertisersApi.md#get_category) | **GET** /v1/advertisers/{advertiserId}/categories/{categoryHashCode} | Gets a specific advertiser&#39;s category
*AudiencesApi* | [**add_remove_users_to_audience**](docs/AudiencesApi.md#add_remove_users_to_audience) | **PATCH** /v1/audiences/userlist/{audienceId} | Add/Remove users to an Audience.
*AudiencesApi* | [**create_audience**](docs/AudiencesApi.md#create_audience) | **POST** /v1/audiences/userlist | Create a new Audience.
*AudiencesApi* | [**delete_audience**](docs/AudiencesApi.md#delete_audience) | **DELETE** /v1/audiences/{audienceId} | Delete an Audience.
*AudiencesApi* | [**get_audiences**](docs/AudiencesApi.md#get_audiences) | **GET** /v1/audiences | Get the list of Audiences.
*AudiencesApi* | [**remove_users_from_audience**](docs/AudiencesApi.md#remove_users_from_audience) | **DELETE** /v1/audiences/userlist/{audienceId}/users | Remove all users from an Audience.
*AudiencesApi* | [**update_audience_metadata**](docs/AudiencesApi.md#update_audience_metadata) | **PUT** /v1/audiences/{audienceId} | Update an Audience metadata.
*AuthenticationApi* | [**o_auth2_token_post**](docs/AuthenticationApi.md#o_auth2_token_post) | **POST** /oauth2/token | Authenticates provided credentials and returns an access token
*BudgetsApi* | [**get**](docs/BudgetsApi.md#get) | **GET** /v1/budgets | Gets budgets
*CampaignsApi* | [**get_bids**](docs/CampaignsApi.md#get_bids) | **GET** /v1/campaigns/bids | Gets a the bids for campaigns and their categories
*CampaignsApi* | [**get_campaign**](docs/CampaignsApi.md#get_campaign) | **GET** /v1/campaigns/{campaignId} | Gets a specific campaign
*CampaignsApi* | [**get_campaigns**](docs/CampaignsApi.md#get_campaigns) | **GET** /v1/campaigns | Gets campaigns
*CampaignsApi* | [**get_categories**](docs/CampaignsApi.md#get_categories) | **GET** /v1/campaigns/{campaignId}/categories | Gets categories
*CampaignsApi* | [**get_category**](docs/CampaignsApi.md#get_category) | **GET** /v1/campaigns/{campaignId}/categories/{categoryHashCode} | Gets a specific category
*CampaignsApi* | [**update_bids**](docs/CampaignsApi.md#update_bids) | **PUT** /v1/campaigns/bids | Update bids for campaigns and their categories
*CategoriesApi* | [**get_categories**](docs/CategoriesApi.md#get_categories) | **GET** /v1/categories | Gets categories
*CategoriesApi* | [**update_categories**](docs/CategoriesApi.md#update_categories) | **PUT** /v1/categories | Enables/disables categories
*PortfolioApi* | [**get_portfolio**](docs/PortfolioApi.md#get_portfolio) | **GET** /v1/portfolio | Gets portfolio
*PublishersApi* | [**get_stats**](docs/PublishersApi.md#get_stats) | **POST** /v1/publishers/stats | 
*SellersApi* | [**create_budgets**](docs/SellersApi.md#create_budgets) | **POST** /v1/sellers/budgets | Creates a budget for a seller/list of sellers.
*SellersApi* | [**get**](docs/SellersApi.md#get) | **GET** /v1/sellers | Gets sellers details.
*SellersApi* | [**get_campaigns**](docs/SellersApi.md#get_campaigns) | **GET** /v1/sellers/campaigns | Gets campaigns
*SellersApi* | [**get_stats**](docs/SellersApi.md#get_stats) | **POST** /v1/sellers/stats | Generates a statistics report
*SellersApi* | [**update_bids**](docs/SellersApi.md#update_bids) | **PUT** /v1/sellers/bids | Set or update a bid for a seller/list of sellers.
*SellersApi* | [**update_budgets**](docs/SellersApi.md#update_budgets) | **PUT** /v1/sellers/budgets | Updates a budget for a seller/list of sellers.
*SellersV2Api* | [**create_seller_budgets**](docs/SellersV2Api.md#create_seller_budgets) | **POST** /v2/crp/budgets | Create a collection of budgets.
*SellersV2Api* | [**create_seller_campaigns_by_seller**](docs/SellersV2Api.md#create_seller_campaigns_by_seller) | **POST** /v2/crp/sellers/{sellerId}/seller-campaigns | Create a SellerCampaign
*SellersV2Api* | [**create_sellers**](docs/SellersV2Api.md#create_sellers) | **POST** /v2/crp/advertisers/{advertiserId}/sellers | Create new sellers for an advertiser
*SellersV2Api* | [**get_advertiser**](docs/SellersV2Api.md#get_advertiser) | **GET** /v2/crp/advertisers/{advertiserId} | Get an advertiser.
*SellersV2Api* | [**get_advertiser_campaigns**](docs/SellersV2Api.md#get_advertiser_campaigns) | **GET** /v2/crp/advertisers/{advertiserId}/campaigns | Get the collection of CRP campaigns associated with the advertiserId.
*SellersV2Api* | [**get_advertiser_preview_limits**](docs/SellersV2Api.md#get_advertiser_preview_limits) | **GET** /v2/crp/advertisers/preview-limit | Get the collection of advertisers preview limits associated with the user.
*SellersV2Api* | [**get_advertisers**](docs/SellersV2Api.md#get_advertisers) | **GET** /v2/crp/advertisers | Get the collection of advertisers associated with the user.
*SellersV2Api* | [**get_budgets_by_advertiser**](docs/SellersV2Api.md#get_budgets_by_advertiser) | **GET** /v2/crp/advertisers/{advertiserId}/budgets | Get CRP budgets for a specific advertiser
*SellersV2Api* | [**get_budgets_by_seller**](docs/SellersV2Api.md#get_budgets_by_seller) | **GET** /v2/crp/sellers/{sellerId}/budgets | Get a collection of budgets for this seller.
*SellersV2Api* | [**get_budgets_by_seller_campaign_id**](docs/SellersV2Api.md#get_budgets_by_seller_campaign_id) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId}/budgets | Get a collection of budgets for this seller campaign.
*SellersV2Api* | [**get_seller**](docs/SellersV2Api.md#get_seller) | **GET** /v2/crp/sellers/{sellerId} | Get details for a seller.
*SellersV2Api* | [**get_seller_budget**](docs/SellersV2Api.md#get_seller_budget) | **GET** /v2/crp/budgets/{budgetId} | Get details for a budget.
*SellersV2Api* | [**get_seller_budgets**](docs/SellersV2Api.md#get_seller_budgets) | **GET** /v2/crp/budgets | Get a collection of budgets.
*SellersV2Api* | [**get_seller_campaign**](docs/SellersV2Api.md#get_seller_campaign) | **GET** /v2/crp/seller-campaigns/{sellerCampaignId} | Get details for a seller campaign.
*SellersV2Api* | [**get_seller_campaigns**](docs/SellersV2Api.md#get_seller_campaigns) | **GET** /v2/crp/seller-campaigns | Get a collection of seller campaigns.
*SellersV2Api* | [**get_seller_campaigns_by_advertiser**](docs/SellersV2Api.md#get_seller_campaigns_by_advertiser) | **GET** /v2/crp/advertisers/{advertiserId}/seller-campaigns | Get CRP seller-campaigns for a specific advertiser
*SellersV2Api* | [**get_seller_campaigns_by_seller**](docs/SellersV2Api.md#get_seller_campaigns_by_seller) | **GET** /v2/crp/sellers/{sellerId}/seller-campaigns | Get a collection of seller campaigns for this seller.
*SellersV2Api* | [**get_sellers**](docs/SellersV2Api.md#get_sellers) | **GET** /v2/crp/sellers | Get a collection of sellers.
*SellersV2Api* | [**update_seller_budget**](docs/SellersV2Api.md#update_seller_budget) | **PATCH** /v2/crp/budgets/{budgetId} | Modify a single budget.
*SellersV2Api* | [**update_seller_budgets**](docs/SellersV2Api.md#update_seller_budgets) | **PATCH** /v2/crp/budgets | Modify a collection of budgets.
*SellersV2Api* | [**update_seller_campaign**](docs/SellersV2Api.md#update_seller_campaign) | **PATCH** /v2/crp/seller-campaigns/{sellerCampaignId} | Update an existing seller campaign.
*SellersV2Api* | [**update_seller_campaigns**](docs/SellersV2Api.md#update_seller_campaigns) | **PATCH** /v2/crp/seller-campaigns | Update a collection of seller campaigns.
*SellersV2StatsApi* | [**campaigns**](docs/SellersV2StatsApi.md#campaigns) | **GET** /v2/crp/stats/campaigns | Get stats by campaign.
*SellersV2StatsApi* | [**seller_campaigns**](docs/SellersV2StatsApi.md#seller_campaigns) | **GET** /v2/crp/stats/seller-campaigns | Get stats by seller-campaign.
*SellersV2StatsApi* | [**sellers**](docs/SellersV2StatsApi.md#sellers) | **GET** /v2/crp/stats/sellers | Get stats by seller.
*StatisticsApi* | [**get_campaign_report**](docs/StatisticsApi.md#get_campaign_report) | **POST** /v1/statistics/report | Generates a statistics report
*StatisticsApi* | [**get_stats**](docs/StatisticsApi.md#get_stats) | **POST** /v1/statistics | Generates a statistics report


## Documentation For Models

 - [AdvertiserCampaignMessage](docs/AdvertiserCampaignMessage.md)
 - [AdvertiserInfoMessage](docs/AdvertiserInfoMessage.md)
 - [AdvertiserQuotaMessage](docs/AdvertiserQuotaMessage.md)
 - [AudienceCreateRequest](docs/AudienceCreateRequest.md)
 - [AudienceCreateResponse](docs/AudienceCreateResponse.md)
 - [AudiencePatchRequest](docs/AudiencePatchRequest.md)
 - [AudiencePatchResponse](docs/AudiencePatchResponse.md)
 - [AudiencePutRequest](docs/AudiencePutRequest.md)
 - [AudienceResponse](docs/AudienceResponse.md)
 - [AudiencesGetResponse](docs/AudiencesGetResponse.md)
 - [BidMessage](docs/BidMessage.md)
 - [BudgetMessage](docs/BudgetMessage.md)
 - [CampaignBidChangeRequest](docs/CampaignBidChangeRequest.md)
 - [CampaignBidChangeResponse](docs/CampaignBidChangeResponse.md)
 - [CampaignBidMessage](docs/CampaignBidMessage.md)
 - [CampaignMessage](docs/CampaignMessage.md)
 - [CampaignReportQueryMessage](docs/CampaignReportQueryMessage.md)
 - [CatalogProduct](docs/CatalogProduct.md)
 - [CatalogProductV3](docs/CatalogProductV3.md)
 - [CategoryBidChangeRequest](docs/CategoryBidChangeRequest.md)
 - [CategoryBidMessage](docs/CategoryBidMessage.md)
 - [CategoryMessage](docs/CategoryMessage.md)
 - [CategoryUpdateError](docs/CategoryUpdateError.md)
 - [CategoryUpdateInput](docs/CategoryUpdateInput.md)
 - [CategoryUpdatesPerCatalog](docs/CategoryUpdatesPerCatalog.md)
 - [CategoryUpdatesPerCatalogError](docs/CategoryUpdatesPerCatalogError.md)
 - [CheckResult](docs/CheckResult.md)
 - [ClientRegistrationRequestMessage](docs/ClientRegistrationRequestMessage.md)
 - [ClientRegistrationResponseMessage](docs/ClientRegistrationResponseMessage.md)
 - [CreateSellerBudgetMapiMessage](docs/CreateSellerBudgetMapiMessage.md)
 - [CreateSellerCampaignMessageMapi](docs/CreateSellerCampaignMessageMapi.md)
 - [CustomAttributeV3](docs/CustomAttributeV3.md)
 - [ErrorSource](docs/ErrorSource.md)
 - [GoogleProduct](docs/GoogleProduct.md)
 - [GoogleProductV3](docs/GoogleProductV3.md)
 - [IThrottlingConfiguration](docs/IThrottlingConfiguration.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Installment](docs/Installment.md)
 - [InstallmentAmount](docs/InstallmentAmount.md)
 - [InstallmentV3](docs/InstallmentV3.md)
 - [LoyaltyPointsV3](docs/LoyaltyPointsV3.md)
 - [LoyatyPoints](docs/LoyatyPoints.md)
 - [MapiUserMessage](docs/MapiUserMessage.md)
 - [MarketplaceCampaignMessage](docs/MarketplaceCampaignMessage.md)
 - [MessageWithDetailsCampaignBidChangeResponse](docs/MessageWithDetailsCampaignBidChangeResponse.md)
 - [MessageWithDetailsCategoryUpdatesPerCatalogError](docs/MessageWithDetailsCategoryUpdatesPerCatalogError.md)
 - [PolicyRouteInfo](docs/PolicyRouteInfo.md)
 - [PortfolioMessage](docs/PortfolioMessage.md)
 - [Price](docs/Price.md)
 - [ProductImporterBatch](docs/ProductImporterBatch.md)
 - [ProductImporterMessage](docs/ProductImporterMessage.md)
 - [ProductShippingDimensionV3](docs/ProductShippingDimensionV3.md)
 - [ProductShippingV3](docs/ProductShippingV3.md)
 - [ProductShippingWeightV3](docs/ProductShippingWeightV3.md)
 - [ProductTaxV3](docs/ProductTaxV3.md)
 - [ProductUnitPricingBaseMeasureV3](docs/ProductUnitPricingBaseMeasureV3.md)
 - [PublisherFileStatsMessage](docs/PublisherFileStatsMessage.md)
 - [PublisherStatsMessage](docs/PublisherStatsMessage.md)
 - [PublisherStatsQueryMessage](docs/PublisherStatsQueryMessage.md)
 - [RoutePolicy](docs/RoutePolicy.md)
 - [SellerBase](docs/SellerBase.md)
 - [SellerBidInfoMessage](docs/SellerBidInfoMessage.md)
 - [SellerBidsMessage](docs/SellerBidsMessage.md)
 - [SellerBudgetCreateMessage](docs/SellerBudgetCreateMessage.md)
 - [SellerBudgetInfoMessage](docs/SellerBudgetInfoMessage.md)
 - [SellerBudgetMessage](docs/SellerBudgetMessage.md)
 - [SellerBudgetResponseMessage](docs/SellerBudgetResponseMessage.md)
 - [SellerBudgetUpdateMessage](docs/SellerBudgetUpdateMessage.md)
 - [SellerBudgetsCreateMessage](docs/SellerBudgetsCreateMessage.md)
 - [SellerBudgetsMessage](docs/SellerBudgetsMessage.md)
 - [SellerBudgetsUpdateMessage](docs/SellerBudgetsUpdateMessage.md)
 - [SellerCampaignMessage](docs/SellerCampaignMessage.md)
 - [SellerCampaignUpdate](docs/SellerCampaignUpdate.md)
 - [SellerInfoMessage](docs/SellerInfoMessage.md)
 - [SellerMessage](docs/SellerMessage.md)
 - [ServiceStatusCheckResult](docs/ServiceStatusCheckResult.md)
 - [Shipping](docs/Shipping.md)
 - [ShippingSize](docs/ShippingSize.md)
 - [StatsQueryMessage](docs/StatsQueryMessage.md)
 - [StatsQueryMessageEx](docs/StatsQueryMessageEx.md)
 - [Tax](docs/Tax.md)
 - [ThrottlePolicy](docs/ThrottlePolicy.md)
 - [ThrottlePolicyRates](docs/ThrottlePolicyRates.md)
 - [UnitMeasure](docs/UnitMeasure.md)
 - [UpdateSellerBudgetMessage](docs/UpdateSellerBudgetMessage.md)
 - [UpdateSellerBudgetMessageBase](docs/UpdateSellerBudgetMessageBase.md)


## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.