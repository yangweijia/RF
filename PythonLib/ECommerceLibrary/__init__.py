from goodsManagePage import goodsManagePage
from loginPage import loginPage
from BasicOperation import BasicOperation
from brandManagePage import brandManagePage
from goodsApprovePage import goodsApprovePage
from orderDeliverConfirmPage import orderDeliverConfirmPage
from orderDeliverMsPage import orderDeliverMsPage
from orderMsPage import orderMsPage
from orderReturnMsPage import orderReturnMsPage
from Search import Search
from superGoodsManagePage import superGoodsManagePage
from Table import Table
from Element import Element
from version import VERSION

_version_ = VERSION

class ECommerceLibrary(loginPage, 
		goodsManagePage, 
		BasicOperation,
		brandManagePage,
		goodsApprovePage,
		orderDeliverConfirmPage,
		orderDeliverMsPage,
		orderMsPage,
		orderReturnMsPage,
		Search,
		superGoodsManagePage,
		Table,
                Element):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
