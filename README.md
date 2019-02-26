# Criteo Marketing SDK for Python
[![Build Status](https://travis-ci.com/criteo/criteo-python-marketing-sdk.svg?branch=master)](https://travis-ci.com/criteo/criteo-python-marketing-sdk)
[![](https://img.shields.io/pypi/pyversions/criteo-marketing.svg)](https://pypi.org/project/criteo-marketing/)

IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v.1.0
- Package version: 1.0.98

## Requirements.

Python 2.7 and 3.4+

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
Please see [examples/authentication.py](examples/authentication.py) for a full example to get a valid token and make a call to the API.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.AdvertisersApi(criteo_marketing.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')

try:
    # Gets all advertiser's campaigns
    api_response = api_instance.get_campaigns(advertiser_id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertisersApi->get_campaigns: %s\n" % e)

```

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
*StatisticsApi* | [**get_stats**](docs/StatisticsApi.md#get_stats) | **POST** /v1/statistics | Generates a statistics report


## Documentation For Models

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
 - [CatalogProduct](docs/CatalogProduct.md)
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
 - [GoogleProduct](docs/GoogleProduct.md)
 - [IThrottlingConfiguration](docs/IThrottlingConfiguration.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Installment](docs/Installment.md)
 - [InstallmentAmount](docs/InstallmentAmount.md)
 - [LoyatyPoints](docs/LoyatyPoints.md)
 - [MapiUserMessage](docs/MapiUserMessage.md)
 - [MessageWithDetailsCampaignBidChangeResponse](docs/MessageWithDetailsCampaignBidChangeResponse.md)
 - [MessageWithDetailsCategoryUpdatesPerCatalogError](docs/MessageWithDetailsCategoryUpdatesPerCatalogError.md)
 - [PolicyRouteInfo](docs/PolicyRouteInfo.md)
 - [PortfolioMessage](docs/PortfolioMessage.md)
 - [Price](docs/Price.md)
 - [ProductImporterMessage](docs/ProductImporterMessage.md)
 - [PublisherFileStatsMessage](docs/PublisherFileStatsMessage.md)
 - [PublisherStatsMessage](docs/PublisherStatsMessage.md)
 - [PublisherStatsQueryMessage](docs/PublisherStatsQueryMessage.md)
 - [RoutePolicy](docs/RoutePolicy.md)
 - [SellerBidInfoMessage](docs/SellerBidInfoMessage.md)
 - [SellerBidsMessage](docs/SellerBidsMessage.md)
 - [SellerBudgetCreateMessage](docs/SellerBudgetCreateMessage.md)
 - [SellerBudgetInfoMessage](docs/SellerBudgetInfoMessage.md)
 - [SellerBudgetResponseMessage](docs/SellerBudgetResponseMessage.md)
 - [SellerBudgetUpdateMessage](docs/SellerBudgetUpdateMessage.md)
 - [SellerBudgetsCreateMessage](docs/SellerBudgetsCreateMessage.md)
 - [SellerBudgetsMessage](docs/SellerBudgetsMessage.md)
 - [SellerBudgetsUpdateMessage](docs/SellerBudgetsUpdateMessage.md)
 - [SellerCampaignMessage](docs/SellerCampaignMessage.md)
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


## Documentation For Authorization


## Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author





## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.