# Copyright 2019 The TensorTrade Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License


from typing import Union
from sympy import Symbol

from .quantity import Quantity
from .trading_pair import TradingPair

registry = {}


class Instrument:
    """A financial instrument for use in trading."""

    def __init__(self, symbol: Union[Symbol, str], precision: int, name: str = None):
        self._symbol = Symbol(symbol) if isinstance(symbol, str) else symbol
        self._precision = precision
        self._name = name

        registry[symbol] = self

    @property
    def symbol(self) -> str:
        return str(self._symbol)

    @property
    def precision(self) -> int:
        return self._precision

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, other: 'Instrument') -> bool:
        return self.symbol == other.symbol and self.precision == other.precision and self.name == other.name

    def __ne__(self, other: 'Instrument') -> bool:
        return self.symbol != other.symbol or self.precision != other.precision or self.name != other.name

    def __rmul__(self, other: float) -> Quantity:
        return Quantity(instrument=self, size=other)

    def __truediv__(self, other):
        if isinstance(other, Instrument):
            return TradingPair(self, other)

    def __hash__(self):
        return hash(self.symbol)

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return str(self)


# Crypto
BTC = Instrument('BTC', 8, 'Bitcoin')
ETH = Instrument('ETH', 8, 'Ethereum')
XRP = Instrument('XRP', 8, 'XRP')
NEO = Instrument('NEO', 8, 'NEO')
BCH = Instrument('BCH', 8, 'Bitcoin Cash')
LTC = Instrument('LTC', 8, 'Litecoin')
ETC = Instrument('ETC', 8, 'Ethereum Classic')
XLM = Instrument('XLM', 8, 'Stellar Lumens')
LINK = Instrument('LINK', 8, 'Chainlink')
ATOM = Instrument('ATOM', 8, 'Cosmos')
DAI = Instrument('DAI', 8, 'Dai')
USDT = Instrument('USDT', 8, 'Tether')

# FX
USD = Instrument('USD', 2, 'U.S. Dollar')
EUR = Instrument('EUR', 2, 'Euro')
JPY = Instrument('JPY', 2, 'Japanese Yen')
KWN = Instrument('KWN', 2, 'Korean Won')
AUD = Instrument('AUD', 2, 'Australian Dollar')

# Commodities
XAU = Instrument('XAU', 2, 'Gold futures')
XAG = Instrument('XAG', 2, 'Silver futures')

# Stocks
AAGIY = Instrument('AAGIY', 2, 'AIA GRP LTD/S ADR')
AAIGF = Instrument('AAIGF', 2, 'AIA Group Ltd')
AAPL = Instrument('AAPL', 2, 'Apple Inc.')
ABBV = Instrument('ABBV', 2, 'AbbVie Inc')
ABT = Instrument('ABT', 2, 'Abbott Laboratories')
ACGBF = Instrument('ACGBF', 2, 'ABC/Shs H Vtg 1.00')
ACGBY = Instrument('ACGBY', 2, 'AGRICULTURAL BK/ADR')
ACN = Instrument('ACN', 2, 'Accenture Plc')
ADBE = Instrument('ADBE', 2, 'Adobe Inc')
AMD = Instrument('AMD', 2, 'Advanced Micro Devices, Inc.')
AMGN = Instrument('AMGN', 2, 'Amgen, Inc.')
AMT = Instrument('AMT', 2, 'American Tower Corporation (REIT)')
AMZN = Instrument('AMZN', 2, 'Amazon.com, Inc.')
ASML = Instrument('ASML', 2, 'ASML Holding NV')
ASMLF = Instrument('ASMLF', 2, 'ASML Holding NV')
AVGO = Instrument('AVGO', 2, 'Broadcom Inc')
AZN = Instrument('AZN', 2, 'AstraZeneca plc')
AZNCF = Instrument('AZNCF', 2, 'AstraZeneca plc')
BABA = Instrument('BABA', 2, 'Alibaba Group Holding Ltd - ADR')
BAC = Instrument('BAC', 2, 'Bank of America Corp')
BAC_PB = Instrument('BAC-PB', 2, 'Bank of America Corp')
BAC_PC = Instrument('BAC-PC', 2, 'Bank of America Corp')
BAC_PE = Instrument('BAC-PE', 2, 'Bank of America Corp')
BAC_PL = Instrument('BAC-PL', 2, 'Bank of America Corp')
BAC_PM = Instrument('BAC-PM', 2, 'Bank of America Corp')
BAC_PN = Instrument('BAC-PN', 2, 'Bank of America Corp')
BBL = Instrument('BBL', 2, 'BHP Group')
BHP = Instrument('BHP', 2, 'BHP Group PLC')
BHPLF = Instrument('BHPLF', 2, 'BHP Group Ltd')
BML_PG = Instrument('BML-PG', 2, 'Bank of America Corp')
BML_PH = Instrument('BML-PH', 2, 'Bank of America Corp')
BML_PJ = Instrument('BML-PJ', 2, 'Bank of America Corp')
BML_PL = Instrument('BML-PL', 2, 'Bank of America Corp')
BMY = Instrument('BMY', 2, 'Bristol-Myers Squibb Co')
BRK_A = Instrument('BRK-A', 2, 'Berkshire Hathaway Inc. Class A')
BRK_B = Instrument('BRK-B', 2, 'Berkshire Hathaway Inc. Class B')
BUD = Instrument('BUD', 2, 'Anheuser Busch Inbev NV')
C = Instrument('C', 2, 'Citigroup Inc.')
C_PJ = Instrument('C-PJ', 2, 'Citigroup Inc.')
C_PK = Instrument('C-PK', 2, 'Citigroup Inc.')
CCI_PA = Instrument('CCI-PA', 2, 'Crown Castle International Corp')
CHL = Instrument('CHL', 2, 'China Mobile Ltd.')
CHLKF = Instrument('CHLKF', 2, 'China Mobile Ltd.')
CHTR = Instrument('CHTR', 2, 'Charter Communications Inc')
CICHF = Instrument('CICHF', 2, 'CHINA CSTR BK/Shs H Vtg 1.00')
CICHY = Instrument('CICHY', 2, 'CHINA CONSTR BK/ADR')
CIHKY = Instrument('CIHKY', 2, 'CHINA MERCHANTS/ADR')
CMCSA = Instrument('CMCSA', 2, 'Comcast Corporation')
COST = Instrument('COST', 2, 'Costco Wholesale Corporation')
CRM = Instrument('CRM', 2, 'salesforce.com, inc.')
CSCO = Instrument('CSCO', 2, 'Cisco Systems, Inc.')
CVX = Instrument('CVX', 2, 'Chevron Corporation')
DHR = Instrument('DHR', 2, 'Danaher Corporation')
DHR_PA = Instrument('DHR-PA', 2, 'Danaher Corporation')
DIS = Instrument('DIS', 2, 'Walt Disney Co')
FB = Instrument('FB', 2, 'Facebook, Inc. Common Stock')
FMX = Instrument('FMX', 2, 'Fomento Económico Mexicano, S.A.B. de C.V.')
GOOG = Instrument('GOOG', 2, 'Alphabet Inc Class C')
GOOGL = Instrument('GOOGL', 2, 'Alphabet Inc Class A')
HD = Instrument('HD', 2, 'Home Depot Inc')
HON = Instrument('HON', 2, 'Honeywell International Inc.')
IBM = Instrument('IBM', 2, 'IBM Common Stock')
IDCBF = Instrument('IDCBF', 2, 'INDUST & COMMER/Shs H Vtg 1.00')
IDCBY = Instrument('IDCBY', 2, 'Industrial & Cmrcl Bnk f China Ltd')
INTC = Instrument('INTC', 2, 'Intel Corporation')
JNJ = Instrument('JNJ', 2, 'Johnson & Johnson')
JPM = Instrument('JPM', 2, 'JPMorgan Chase & Co.')
JPM_PC = Instrument('JPM-PC', 2, 'JPMorgan Chase & Co.')
JPM_PD = Instrument('JPM-PD', 2, 'JPMorgan Chase & Co.')
JPM_PG = Instrument('JPM-PG', 2, 'JPMorgan Chase & Co.')
JPM_PH = Instrument('JPM-PH', 2, 'JPMorgan Chase & Co.')
JPM_PJ = Instrument('JPM-PJ', 2, 'JPMorgan Chase & Co.')
KO = Instrument('KO', 2, 'Coca-Cola Co')
LFC = Instrument('LFC', 2, 'China Life Insurance Company Limited')
LIN = Instrument('LIN', 2, 'Linde plc')
LLY = Instrument('LLY', 2, 'Eli Lilly And Co')
LMT = Instrument('LMT', 2, 'Lockheed Martin Corporation')
LOW = Instrument('LOW', 2, 'Lowes Companies, Inc.')
LRLCY = Instrument('LRLCY', 2, 'L OREAL S A/ADR')
LVMUY = Instrument('LVMUY', 2, 'LVMH Moet Hennessy Louis Vuitton SA Unsponsored ADR')
MA = Instrument('MA', 2, 'Mastercard Incorporated')
MCD = Instrument('MCD', 2, 'Mcdonalds Corp')
MDT = Instrument('MDT', 2, 'Medtronic PLC')
MPNGF = Instrument('MPNGF', 2, 'Meituan Dianping')
MRK = Instrument('MRK', 2, 'Merck & Co., Inc.')
MSFT = Instrument('MSFT', 2, 'Microsoft Corporation')
NEE = Instrument('NEE', 2, 'NextEra Energy Inc')
NEE_PK = Instrument('NEE-PK', 2, 'NextEra Energy Inc')
NEE_PP = Instrument('NEE-PP', 2, 'NextEra Energy Inc')
NFLX = Instrument('NFLX', 2, 'Netflix Inc')
NKE = Instrument('NKE', 2, 'Nike Inc')
NSRGF = Instrument('NSRGF', 2, 'Nestle SA')
NSRGY = Instrument('NSRGY', 2, 'NESTLE S A/S ADR')
NVDA = Instrument('NVDA', 2, 'NVIDIA Corporation')
NVO = Instrument('NVO', 2, 'Novo Nordisk A/S')
NVS = Instrument('NVS', 2, 'Novartis AG')
NVSEF = Instrument('NVSEF', 2, 'Novartis AG')
ORCL = Instrument('ORCL', 2, 'Oracle Corporation')
PDD = Instrument('PDD', 2, 'Pinduoduo Inc.')
PEP = Instrument('PEP', 2, 'PepsiCo, Inc.')
PFE = Instrument('PFE', 2, 'Pfizer Inc.')
PG = Instrument('PG', 2, 'Procter & Gamble Co')
PM = Instrument('PM', 2, 'Philip Morris International Inc.')
PNGAY = Instrument('PNGAY', 2, 'PING AN INS GRP/S ADR')
PROSF = Instrument('PROSF', 2, 'Prosus NV')
PROSY = Instrument('PROSY', 2, 'PROSUS N V/ADR')
PTR = Instrument('PTR', 2, 'PetroChina Company Limited ADR')
PYPL = Instrument('PYPL', 2, 'Paypal Holdings Inc')
QCOM = Instrument('QCOM', 2, 'QUALCOMM, Inc.')
RDS_A = Instrument('RDS-A', 2, 'Royal Dutch Shell plc ADR Class A')
RDS_B = Instrument('RDS-B', 2, 'Royal Dutch Shell plc ADR Class B')
RHHBY = Instrument('RHHBY', 2, 'Roche Holdings AG Basel ADR Common Stock')
RHHVF = Instrument('RHHVF', 2, 'Roche Holding AG Genussscheine')
RIO = Instrument('RIO', 2, 'Rio Tinto Group')
RY = Instrument('RY', 2, 'Royal Bank of Canada')
RYDAF = Instrument('RYDAF', 2, 'Royal Dutch Shell Plc')
SAP = Instrument('SAP', 2, 'SAP SE')
SAPGF = Instrument('SAPGF', 2, 'SAP SE')
SBUX = Instrument('SBUX', 2, 'Starbucks Corporation')
SFTBF = Instrument('SFTBF', 2, 'SoftBank Group Corp')
SFTBY = Instrument('SFTBY', 2, 'SoftBank Group Corp - ADR')
SHOP = Instrument('SHOP', 2, 'Shopify Inc')
SNY = Instrument('SNY', 2, 'Sanofi')
SSNLF = Instrument('SSNLF', 2, 'Samsung Electronics Co., Ltd.')
T = Instrument('T', 2, 'AT&T Inc.')
TBC = Instrument('TBC', 2, 'AT&T Inc. 5.625% Global Notes d')
TCEHY = Instrument('TCEHY', 2, 'TENCENT HOLDING/ADR')
TCTZF = Instrument('TCTZF', 2, 'Tencent Holdings Ltd')
TM = Instrument('TM', 2, 'Toyota Motor Corp')
TMO = Instrument('TMO', 2, 'Thermo Fisher Scientific Inc.')
TMUS = Instrument('TMUS', 2, 'T-Mobile Us Inc')
TOT = Instrument('TOT', 2, 'TOTAL SE')
TOYOF = Instrument('TOYOF', 2, 'Toyota Motor Corp')
TSLA = Instrument('TSLA', 2, 'Tesla Inc')
TSM = Instrument('TSM', 2, 'Taiwan Semiconductor Manufacturing Company Limited')
TTFNF = Instrument('TTFNF', 2, 'Total SE')
TXN = Instrument('TXN', 2, 'Texas Instruments Incorporated')
UL = Instrument('UL', 2, 'The Unilever Group')
UN = Instrument('UN', 2, 'The Unilever Group')
UNH = Instrument('UNH', 2, 'UnitedHealth Group Inc')
UNP = Instrument('UNP', 2, 'Union Pacific Corporation')
UPS = Instrument('UPS', 2, 'United Parcel Service, Inc.')
V = Instrument('V', 2, 'Visa Inc.')
VZ = Instrument('VZ', 2, 'Verizon Communications Inc.')
WMT = Instrument('WMT', 2, 'Walmart Inc')
XOM = Instrument('XOM', 2, 'Exxon Mobil Corporation')

SPY = Instrument('SPY', 2, 'SPY Index')
