package com.spring.ecommerce.controller;

import com.spring.ecommerce.dto.*;
import com.spring.ecommerce.service.VenditoreService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/venditori")
public class VenditoreController {
    private final VenditoreService service;

    public VenditoreController(VenditoreService service) {
        this.service = service;
    }

    @PostMapping
    public VenditoreDTO creaVenditore(@RequestBody VenditoreDTO dto) {
        return service.aggiungiVenditore(dto);
    }

    @GetMapping("/{id}")
    public VenditoreDTO getVenditore(@PathVariable Long id) {
        return service.getVenditore(id);
    }

    @GetMapping("/{id}/base")
    public VenditoreBaseDTO getBase(@PathVariable Long id) {
        return service.getVenditoreBase(id);
    }

    @PatchMapping("/{id}/password")
    public VenditoreDTO aggiornaPassword(@PathVariable Long id, @RequestBody String nuovaPassword) {
        return service.aggiornaPassword(id, nuovaPassword);
    }

    @PostMapping("/{id}/prodotti")
    public ProdottoDTO aggiungiProdotto(@PathVariable Long id, @RequestBody ProdottoDTO dto) {
        return service.aggiungiProdotto(id, dto);
    }

    @PatchMapping("/prodotti/{id}/quantita")
    public ProdottoDTO aggiornaQuantita(@PathVariable Long id, @RequestBody int nuovaQuantita) {
        return service.aggiornaQuantitaProdotto(id, nuovaQuantita);
    }
}
