package com.spring.prodotto.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.spring.prodotto.dao.ProdottoDAO;
import com.spring.prodotto.dto.ProdottoDTO;
import com.spring.prodotto.dto.ProdottoNoIdDTO;
import com.spring.prodotto.dto.ReportDTO;
import com.spring.prodotto.utility.Conversione;


@Service
public class ProdottoService {
	private final ProdottoDAO prodottoDAO;

	public ProdottoService(ProdottoDAO prodottoDAO) {
		this.prodottoDAO = prodottoDAO;
	}

	public void aggiungiProdotto(ProdottoDTO prodottoDTO) {
		prodottoDAO.salva(Conversione.convertiDaDTO(prodottoDTO));
	}

	public List<ProdottoNoIdDTO> ottieniTuttiProdotti() {
		return prodottoDAO.trovaTutti().stream().map(Conversione::convertiNoIdDTO).collect(Collectors.toList());
	}

	public ProdottoDTO ottieniProdottoPerId(int id) {
		return Conversione.convertiInDTO(prodottoDAO.trovaPerId(id));
	}

	public ReportDTO generaReport() {
		return Conversione.generaReportDaProdotti(prodottoDAO.trovaTutti());
	}
}
