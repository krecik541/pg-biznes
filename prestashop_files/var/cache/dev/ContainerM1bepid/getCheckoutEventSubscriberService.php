<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'PrestaShop\Module\PrestashopCheckout\Checkout\EventSubscriber\CheckoutEventSubscriber' shared service.

return $this->services['PrestaShop\\Module\\PrestashopCheckout\\Checkout\\EventSubscriber\\CheckoutEventSubscriber'] = new \PrestaShop\Module\PrestashopCheckout\Checkout\EventSubscriber\CheckoutEventSubscriber(${($_ = isset($this->services['PrestaShop\\Module\\PrestashopCheckout\\Checkout\\CheckoutChecker']) ? $this->services['PrestaShop\\Module\\PrestashopCheckout\\Checkout\\CheckoutChecker'] : $this->load('getCheckoutCheckerService.php')) && false ?: '_'}, ${($_ = isset($this->services['ps_checkout.bus.command']) ? $this->services['ps_checkout.bus.command'] : $this->load('getPsCheckout_Bus_CommandService.php')) && false ?: '_'}, ${($_ = isset($this->services['PrestaShop\\Module\\PrestashopCheckout\\Repository\\PsCheckoutCartRepository']) ? $this->services['PrestaShop\\Module\\PrestashopCheckout\\Repository\\PsCheckoutCartRepository'] : $this->load('getPsCheckoutCartRepositoryService.php')) && false ?: '_'});
